"""Tolerance response schemas."""

from pydantic import BaseModel, computed_field


class ToleranceResponseSchema(BaseModel):
    """The common response tolerance schema."""

    id: str
    iso_letter: str
    iso_digit: int
    system: str

    @computed_field
    @property
    def full_name(self) -> str:
        """Combine full tolerance name."""
        return f"{self.iso_letter}{self.iso_digit}"
