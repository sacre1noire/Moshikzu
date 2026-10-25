from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.database_url

# Все даты отдаём в UTC, независимо от часового пояса, настроенного в PostgreSQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"options": "-c timezone=UTC"}
)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
