from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Connection(Base):
    __tablename__ = "connections"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    host: Mapped[str] = mapped_column()
    port: Mapped[int] = mapped_column()
    database: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    runs: Mapped[list["AnalysisRun"]] = relationship(
        back_populates="connection", cascade="all, delete-orphan", passive_deletes=True
    )
    query_logs: Mapped[list["QueryLogEntry"]] = relationship(
        back_populates="connection", cascade="all, delete-orphan", passive_deletes=True
    )
