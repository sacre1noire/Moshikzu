from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Severity = Literal["low", "medium", "high"]


class FindingCreate(BaseModel):
    table_name: str = Field(min_length=1, max_length=255)
    severity: Severity
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1)


class FindingUpdate(BaseModel):
    table_name: str | None = Field(default=None, min_length=1, max_length=255)
    severity: Severity | None = None
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)


class FindingRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    run_id: int
    table_name: str
    severity: Severity
    title: str
    description: str
