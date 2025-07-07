"""Tolerance calculators."""

import math
from typing import TYPE_CHECKING

from app.schemas import ToleranceValueRepoSchema

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


async def calculate_deviations_localized(
    i18n: "TranslatorRunner",
    target_value: float,
    tolerance_value: type[ToleranceValueRepoSchema],
) -> str:
    """Calculate dimensional deviations."""

    def fmt(val: float) -> str:
        return f"{val:.10f}".rstrip("0").rstrip(".").replace(".", ",")

    def count_decimal_places(value: float) -> int:
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
    cutting_speed: float,
    tool_diameter: float,
) -> float:
    """Вычисляет частоту вращения шпинделя (об/мин) по скорости резания и диаметру."""
    return round((1000 * cutting_speed) / (math.pi * tool_diameter), 0)


async def calculate_feed_rate(
    spindle_speed: float,
    number_of_teeth: int,
    feed_per_tooth: float,
) -> float:
    """Вычисляет минутную подачу (мм/мин) по частоте вращения, количеству зубьев и подаче на зуб."""
    return round((spindle_speed * number_of_teeth * feed_per_tooth), 0)


async def calculate_feed_per_tooth(
    feed_rate: float,
    spindle_speed: float,
    number_of_teeth: int,
) -> float:
    """Вычисляет подачу на зуб (мм/зуб), если известны минутная подача, частота вращения и количество зубьев."""
    if spindle_speed <= 0 or number_of_teeth <= 0:
        raise ValueError(
            "Spindle speed and number of teeth must be greater than zero."
        )
    return round(feed_rate / (spindle_speed * number_of_teeth), 3)


async def calculate_cutting_speed(
    spindle_speed: float,
    tool_diameter: float,
) -> float:
    """Вычисляет скорость резания (м/мин), если известны частота вращения и диаметр фрезы."""
    return round((math.pi * tool_diameter * spindle_speed) / 1000, 1)
