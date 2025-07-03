"""Tolerance response schemas."""

from pydantic import BaseModel


class OldToleranceResponseSchema(BaseModel):
    """The common response old tolerance schema."""

    name: str
