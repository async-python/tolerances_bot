"""ToleranceMatch input schemas."""

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ToleranceMatchCreateSchema(BaseModel):
    """The common create tolerance match schema."""

    id: UUID = Field(default_factory=uuid4)
    tolerance_id: UUID
    old_tolerance_id: UUID


class ToleranceMatchSearchSchema(BaseModel):
    """The input tolerance match schema for search."""

    tolerance_id: UUID
    old_tolerance_id: UUID


class ToleranceMatchSearchIdSchema(BaseModel):
    """The input tolerance match schema for search by id."""

    id: UUID
