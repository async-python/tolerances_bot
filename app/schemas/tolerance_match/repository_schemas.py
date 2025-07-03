"""ToleranceMatch db schemas."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ToleranceMatchRepoSchema(BaseModel):
    """The common db tolerance match schema."""

    id: UUID
    tolerance_id: UUID
    old_tolerance_id: UUID
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
