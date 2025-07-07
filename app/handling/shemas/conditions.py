"""Conditions schemas."""

from pydantic import BaseModel, Field, model_validator


class ConditionSchema(BaseModel):
    """The common conditions schema."""

    tool_diameter: float | None = Field(default=None)
    cutting_speed: float | None = Field(default=None)
    spindle_speed: float | None = Field(default=None)
    number_of_teeth: int | None = Field(default=None)
    feed_per_tooth: float | None = Field(default=None)
    feed_rate: float | None = Field(default=None)

    @model_validator(mode="before")
    @classmethod
    def replace_commas(cls, data):
        """Автоматически заменяет ',' на '.' в строках, если поле ожидает float."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and "," in value:
                    data[key] = value.replace(",", ".")
        return data
