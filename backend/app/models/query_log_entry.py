from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class QueryLogEntry(Base):
    __tablename__ = "query_log_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    connection_id: Mapped[int] = mapped_column(ForeignKey("connections.id", ondelete="CASCADE"))
    query: Mapped[str] = mapped_column(Text)
    is_anomaly: Mapped[bool] = mapped_column(default=False)
    executed_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    connection: Mapped["Connection"] = relationship(back_populates="query_logs")
