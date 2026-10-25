# Smart Database Schema Analyzer, рабочее название проекта "Moshikzu"

## Назначение
Smart Database Schema Analyzer — инструмент для разработчиков, который подключается 
к базе данных PostgreSQL, строит визуальную схему связей между таблицами (ER-граф) 
и автоматически находит потенциальные проблемы: отсутствующие индексы, слишком часто 
меняющиеся таблицы, структурные риски. Отдельный модуль анализирует текст выполняемых 
SQL-запросов через ML-эмбеддинги и выявляет аномальные/нетипичные запросы.

## Пользовательские сценарии
1. Пользователь подключает базу данных (указывает параметры подключения).
2. Система строит ER-граф — визуализацию таблиц и связей между ними.
3. Пользователь просматривает список находок (проблемы со схемой: индексация, 
   часто изменяемые таблицы и т.д.).
4. Пользователь открывает карточку конкретной таблицы — видит её столбцы, индексы, 
   связи и историю изменений.
5. Пользователь просматривает журнал выполненных запросов и отмеченные системой 
   как аномальные (ML-модуль на эмбеддингах).
6. Пользователь сравнивает результаты анализа между разными подключениями/периодами.

## Экраны
- Список подключений / Dashboard
- Форма подключения к БД
- ER-граф схемы
- Список находок (Findings)
- Детали таблицы
- Журнал запросов и аномалии

## Стек
- Frontend: React + TypeScript, Vite, Mantine, React Router, React Flow
- Backend: Python + FastAPI
- База данных: PostgreSQL + SQLAlchemy 2.0, миграции через Alembic
- Конфигурация: pydantic-settings (`.env`)

## Структура репозитория
```
frontend/                 React-приложение
backend/
  .env.example            пример настроек (без секретов)
  requirements.txt        зависимости Python
  alembic.ini, alembic/   миграции БД
  app/
    main.py               создание приложения, подключение роутеров
    core/config.py        конфигурация (читает .env)
    core/errors.py        ошибка нарушения бизнес-правила (→ 409)
    db/                   подключение к БД и сессии (session.py), базовый класс моделей (base.py)
    models/               модели SQLAlchemy (таблицы)
    schemas/              схемы Pydantic — валидация запросов и ответов
    services/             операции с данными (CRUD)
    api/routes/           маршруты API
    api/deps.py           общие проверки (запись не найдена → 404)
docs/                     скриншоты
```

## Модель данных

```
connections
  ├── analysis_runs
  │     └── findings
  └── query_log_entries
```

| Таблица | Назначение | Поля |
|---|---|---|
| `connections` | параметры подключения к анализируемой БД | `id` (PK), `name`, `host`, `port`, `database`, `username`, `password`, `created_at` |
| `analysis_runs` | запуск анализа для подключения | `id` (PK), `connection_id` (FK → `connections.id`), `status` (`pending` / `running` / `done` / `failed`), `tables_count` (может быть пустым), `started_at`, `finished_at` (может быть пустым) |
| `findings` | проблема, найденная при анализе | `id` (PK), `run_id` (FK → `analysis_runs.id`), `table_name`, `severity` (`low` / `medium` / `high`), `title`, `description` |
| `query_log_entries` | SQL-запрос из журнала подключения | `id` (PK), `connection_id` (FK → `connections.id`), `query`, `is_anomaly`, `executed_at` |

Связи:
- одно подключение → много запусков анализа и много записей журнала запросов;
- один запуск анализа → много находок;
- все внешние ключи с `ON DELETE CASCADE`: при удалении подключения удаляются его запуски, их находки и журнал запросов; при удалении запуска — его находки.

Пароль подключения хранится в БД, но не возвращается ни в одном ответе API.
Все даты хранятся с часовым поясом и отдаются API в UTC.

### Бизнес-правила запуска анализа
Реализованы в `app/services/analysis_runs.py` и `app/services/findings.py`:
- новый запуск всегда создаётся со статусом `pending`;
- статус меняется только вперёд: `pending → running → done`, а также `pending → failed` и `running → failed`;
- завершённый запуск (`done` / `failed`) изменить нельзя;
- `finished_at` проставляется автоматически при переходе в `done` или `failed`;
- `tables_count` указывается только при переходе в `done`;
- находки можно добавлять только в запуск со статусом `running` или `done`.

Нарушение правила → ответ `409 Conflict` с описанием причины.

## Запуск backend

Требуется Python 3.12+ и PostgreSQL.

### 1. Подготовить PostgreSQL

Запустить сервер (пример для Arch/Manjaro; при первой установке перед этим один раз выполнить
`sudo -iu postgres initdb -D /var/lib/postgres/data`):
```bash
sudo systemctl enable --now postgresql
```

Создать пользователя и базу (пароль — свой):
```bash
sudo -u postgres psql -c "CREATE USER moshikzu WITH PASSWORD 'your_password';"
sudo -u postgres psql -c "CREATE DATABASE moshikzu OWNER moshikzu;"
```

### 2. Настроить окружение
```bash
cd backend
cp .env.example .env
```
В `.env` указать свой пароль в `DATABASE_URL`:
```
DATABASE_URL=postgresql+psycopg://moshikzu:your_password@localhost:5432/moshikzu
```
Файл `.env` в git не попадает.

### 3. Установить зависимости
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Создать таблицы
```bash
alembic upgrade head
```
Команда применяет все миграции из `alembic/versions/` и создаёт таблицы в БД.

### 5. Запустить сервер
```bash
fastapi dev app/main.py
```
- API: `http://localhost:8000`
- Документация и проверка запросов (Swagger): `http://localhost:8000/docs`
- Проверка подключения к БД: `http://localhost:8000/health/db`

### Возможная проблема
Если после обновления системы PostgreSQL пишет `collation version mismatch`, нужно обновить версию
сортировки для указанной базы (пример для `template1`):
```bash
sudo -u postgres psql -d template1 -c "REINDEX DATABASE template1;" -c "ALTER DATABASE template1 REFRESH COLLATION VERSION;"
```

## API

| Метод | Адрес | Действие |
|---|---|---|
| `POST` / `GET` | `/connections` | создать подключение / список |
| `GET` / `PATCH` / `DELETE` | `/connections/{connection_id}` | получить / изменить / удалить |
| `POST` / `GET` | `/connections/{connection_id}/runs` | создать запуск анализа (без тела) / запуски подключения |
| `GET` / `PATCH` / `DELETE` | `/runs/{run_id}` | получить / изменить / удалить |
| `POST` / `GET` | `/runs/{run_id}/findings` | создать находку / находки запуска |
| `GET` / `PATCH` / `DELETE` | `/findings/{finding_id}` | получить / изменить / удалить |
| `POST` / `GET` | `/connections/{connection_id}/query-logs` | добавить запрос в журнал / журнал подключения |
| `GET` / `PATCH` / `DELETE` | `/query-logs/{entry_id}` | получить / изменить / удалить |
| `GET` | `/health`, `/health/db` | проверка работы сервера и БД |

Коды ответов:
- `201` — запись создана, `204` — запись удалена;
- `404` — запись (или родительская запись) не найдена;
- `409` — действие нарушает бизнес-правило (например, недопустимая смена статуса запуска);
- `422` — некорректные данные (с описанием, какое поле и что не так);
- `503` — база данных недоступна.

`PATCH` меняет только переданные поля. Списки отдаются от новых записей к старым.

## Запуск frontend

1. Перейти в папку frontend: `cd frontend`
2. Установить зависимости: `npm install`
3. Запустить дев-сервер: `npm run dev`
4. Открыть в браузере адрес, который выведет терминал (`http://localhost:5173`).
