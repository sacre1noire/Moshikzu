from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class AnalysisRun(Base):
    __tablename__ = "analysis_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    connection_id: Mapped[int] = mapped_column(ForeignKey("connections.id", ondelete="CASCADE"))
    status: Mapped[str] = mapped_column(String(50))
    tables_count: Mapped[int | None] = mapped_column()
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    connection: Mapped["Connection"] = relationship(back_populates="runs")
    findings: Mapped[list["Finding"]] = relationship(
        back_populates="run", cascade="all, delete-orphan", passive_deletes=True
    )
