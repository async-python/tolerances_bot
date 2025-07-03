"""Tolerance input schemas."""

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class OldToleranceCreateSchema(BaseModel):
    """The common create old tolerance schema."""

    id: UUID = Field(default_factory=uuid4)
    name: str


class OldToleranceMappingShema(BaseModel):
    """The common create old tolerance schema."""

    name: str
    new_name: str


class OldToleranceSearchShema(BaseModel):
    """The input old tolerance schema for search."""

    name: str


class OldToleranceSearchIdShema(BaseModel):
    """The input old tolerance schema for search by id."""

    id: UUID
