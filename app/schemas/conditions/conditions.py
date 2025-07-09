"""Conditions schemas."""

from decimal import Decimal

from pydantic import BaseModel, Field, model_validator


class ConditionSchema(BaseModel):
    """The common conditions schema."""

    tool_diameter: Decimal | None = Field(default=None)
    cutting_speed: Decimal | None = Field(default=None)
    spindle_speed: Decimal | None = Field(default=None)
    number_of_teeth: int | None = Field(default=None)
    feed_per_tooth: Decimal | None = Field(default=None)
    feed_rate: Decimal | None = Field(default=None)

    @model_validator(mode="before")
    @classmethod
    def replace_commas(cls: object, data: dict) -> dict:
        """Automatically replaces ',' with '.' in strings
        if the field expects a float."""
        for key, value in data.items():
            if isinstance(value, str) and "," in value:
                data[key] = value.replace(",", ".")
        return data
