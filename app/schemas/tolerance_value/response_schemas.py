"""ToleranceMatch response schemas."""

from pydantic import BaseModel


class ToleranceValueResponseSchema(BaseModel):
    """The common response tolerance value schema."""

    upper_value: float
    lower_value: float
