"""ToleranceValue input schemas."""

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ToleranceValueCreateSchema(BaseModel):
    """The common create tolerance value schema."""

    id: UUID = Field(default_factory=uuid4)
    tolerance_id: UUID
    range_id: UUID
    upper_value: float
    lower_value: float


class ToleranceValueSearchSchema(BaseModel):
    """The input tolerance value schema for search."""

    tolerance_id: UUID
    range_id: UUID


class ToleranceValueSearchIdSchema(BaseModel):
    """The input tolerance value schema for search by id."""

    id: UUID
