from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ConnectionCreate(BaseModel):
    name: str = Field(min_length=1)
    host: str = Field(min_length=1)
    port: int = Field(ge=1, le=65535)
    database: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class ConnectionUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    host: str | None = Field(default=None, min_length=1)
    port: int | None = Field(default=None, ge=1, le=65535)
    database: str | None = Field(default=None, min_length=1)
    username: str | None = Field(default=None, min_length=1)
    password: str | None = Field(default=None, min_length=1)


class ConnectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    host: str
    port: int
    database: str
    username: str
    created_at: datetime
