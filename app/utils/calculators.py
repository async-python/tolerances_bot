"""Tolerance calculators."""

import math
from decimal import Decimal
from typing import TYPE_CHECKING

from app.schemas import ToleranceValueRepoSchema

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


async def calculate_deviations_localized(
    i18n: "TranslatorRunner",
    target_value: Decimal,
    tolerance_value: type[ToleranceValueRepoSchema],
) -> str:
    """Calculate dimensional deviations."""

    def fmt(val: Decimal) -> str:
        return f"{val:.10f}".rstrip("0").rstrip(".").replace(".", ",")

    def count_decimal_places(value: Decimal) -> int:
        s = f"{value:.10f}".rstrip("0")
        if "." in s:
            return len(s.split(".")[1])
        return 0

    upper_decimals = count_decimal_places(tolerance_value.upper_value)
    lower_decimals = count_decimal_places(tolerance_value.lower_value)
    precision = max(upper_decimals, lower_decimals) + 1

    avg_value = round(
        target_value
        + (tolerance_value.upper_value + tolerance_value.lower_value) / 2,
        precision,
    )

    return i18n.tolerance.answer(
        upper=fmt(tolerance_value.upper_value),
        lower=fmt(tolerance_value.lower_value),
        max=fmt(target_value + tolerance_value.upper_value),
        avg=fmt(avg_value),
        min=fmt(target_value + tolerance_value.lower_value),
    )


async def calculate_spindle_speed(
    cutting_speed: Decimal,
    tool_diameter: Decimal,
) -> Decimal:
    """Calculates the spindle speed (rpm) based on the
    cutting speed and diameter."""
    return round((1000 * cutting_speed) / (Decimal(math.pi) * tool_diameter), 0)


async def calculate_feed_rate(
    spindle_speed: Decimal,
    number_of_teeth: int,
    feed_per_tooth: Decimal,
) -> Decimal:
    """Calculates the minute feed (mm/min) based on rotation speed,
    number of teeth and feed per tooth."""
    return round((spindle_speed * number_of_teeth * feed_per_tooth), 0)


async def calculate_feed_per_tooth(
    feed_rate: Decimal,
    spindle_speed: Decimal,
    number_of_teeth: int,
) -> Decimal:
    """Calculates the feed per tooth (mm/tooth) if the minute feed,
    rotation speed and number of teeth are known."""
    if spindle_speed <= 0 or number_of_teeth <= 0:
        raise ValueError(
            "Spindle speed and number of teeth must be greater than zero."
        )
    return round(feed_rate / (spindle_speed * number_of_teeth), 3)


async def calculate_cutting_speed(
    spindle_speed: Decimal,
    tool_diameter: Decimal,
) -> Decimal:
    """Calculates the cutting speed (m/min) if the rotation speed
    and diameter of the milling cutter are known."""
    return round((Decimal(math.pi) * tool_diameter * spindle_speed) / 1000, 1)
