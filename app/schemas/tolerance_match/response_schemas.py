"""ToleranceMatch response schemas."""

from uuid import UUID

from pydantic import BaseModel


class ToleranceMatchResponseSchema(BaseModel):
    """The common response tolerance value schema."""

    tolerance_id: UUID
    old_tolerance_id: UUID
