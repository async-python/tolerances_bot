"""ToleranceMatch db schemas."""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ToleranceValueRepoSchema(BaseModel):
    """The common db tolerance value schema."""

    id: UUID
    tolerance_id: UUID
    range_id: UUID
    upper_value: Decimal
    lower_value: Decimal
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
