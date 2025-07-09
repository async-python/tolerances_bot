"""ToleranceMatch response schemas."""

from decimal import Decimal

from pydantic import BaseModel


class ToleranceValueResponseSchema(BaseModel):
    """The common response tolerance value schema."""

    upper_value: Decimal
    lower_value: Decimal
