"""Tolerance db schemas."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.constants.db_enums import SystemType
from app.schemas import OldToleranceRepoSchema, RangeRepoSchema


class ToleranceRepoSchema(BaseModel):
    """The common db tolerance schema."""

    id: UUID
    iso_letter: str
    iso_digit: int
    system: SystemType
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class ToleranceRepoRelatedOldTolSchema(BaseModel):
    """The common db tolerance schema with relatives."""

    id: UUID
    iso_letter: str
    iso_digit: int
    system: SystemType
    created_at: datetime
    updated_at: datetime | None

    linked_old_tolerances: list[OldToleranceRepoSchema] | None

    model_config = ConfigDict(from_attributes=True)


class ToleranceRepoRelatedRangesSchema(BaseModel):
    """The common db tolerance schema with relatives."""

    id: UUID
    iso_letter: str
    iso_digit: int
    system: SystemType
    created_at: datetime
    updated_at: datetime | None

    linked_ranges: list[RangeRepoSchema] | None

    model_config = ConfigDict(from_attributes=True)
