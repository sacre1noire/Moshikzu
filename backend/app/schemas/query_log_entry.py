from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class QueryLogEntryCreate(BaseModel):
    query: str = Field(min_length=1)
    is_anomaly: bool = False


class QueryLogEntryUpdate(BaseModel):
    query: str | None = Field(default=None, min_length=1)
    is_anomaly: bool | None = None


class QueryLogEntryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    connection_id: int
    query: str
    is_anomaly: bool
    executed_at: datetime
