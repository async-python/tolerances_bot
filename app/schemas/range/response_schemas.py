"""Range response schemas."""

from pydantic import BaseModel


class RangeResponseSchema(BaseModel):
    """The common response range schema."""

    min_value: int
    max_value: int
