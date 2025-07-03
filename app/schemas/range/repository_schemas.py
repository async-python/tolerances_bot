"""Range db schemas."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RangeRepoSchema(BaseModel):
    """The common db range schema."""

    id: UUID
    min_value: int
    max_value: int
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
