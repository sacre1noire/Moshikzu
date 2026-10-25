from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

RunStatus = Literal["pending", "running", "done", "failed"]


class AnalysisRunUpdate(BaseModel):
    status: RunStatus | None = None
    tables_count: int | None = Field(default=None, ge=0)


class AnalysisRunRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    connection_id: int
    status: RunStatus
    tables_count: int | None
    started_at: datetime
    finished_at: datetime | None
