"""ToleranceValue input schemas."""

from decimal import Decimal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ToleranceValueCreateSchema(BaseModel):
    """The common create tolerance value schema."""

    id: UUID = Field(default_factory=uuid4)
    tolerance_id: UUID
    range_id: UUID
    upper_value: Decimal
    lower_value: Decimal


class ToleranceValueSearchSchema(BaseModel):
    """The input tolerance value schema for search."""

    tolerance_id: UUID
    range_id: UUID


class ToleranceValueSearchIdSchema(BaseModel):
    """The input tolerance value schema for search by id."""

    id: UUID
