from sqlalchemy.orm import DeclarativeBase

# Максимум для типа integer в PostgreSQL: число больше этого база не примет
MAX_INT = 2_147_483_647


class Base(DeclarativeBase):
    pass
