"""ToleranceMatch db schemas."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ToleranceValueRepoSchema(BaseModel):
    """The common db tolerance value schema."""

    id: UUID
    tolerance_id: UUID
    range_id: UUID
    upper_value: float
    lower_value: float
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
