"""Tolerance input schemas."""

from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.constants.model_enums import SystemType


class ToleranceCreateSchema(BaseModel):
    """The common create tolerance schema."""

    id: UUID = Field(default_factory=uuid4)
    iso_letter: str
    iso_digit: int
    system: SystemType


class ToleranceSearchSchema(BaseModel):
    """The input tolerance schema for search."""

    iso_letter: str
    iso_digit: int


class ToleranceSearchIdData(BaseModel):
    """The input tolerance schema for search by id."""

    id: UUID
