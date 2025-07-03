"""Range input schemas."""

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class RangeCreateSchema(BaseModel):
    """The common create range schema."""

    id: UUID = Field(default_factory=uuid4)
    min_value: int
    max_value: int


class RangeSearchSchema(BaseModel):
    """The input range schema for search."""

    min_value: int
    max_value: int


class RangeSearchIdSchema(BaseModel):
    """The input range schema for search by id."""

    id: UUID
