"""Tolerance db schemas."""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.schemas import ToleranceRepoSchema


class OldToleranceRepoSchema(BaseModel):
    """The common db old tolerance schema."""

    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class OldToleranceRepoRelatedSchema(BaseModel):
    """The common db old tolerance schema with relatives."""

    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime | None

    linked_tolerances: list["ToleranceRepoSchema"] | None

    model_config = ConfigDict(from_attributes=True)
