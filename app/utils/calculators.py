"""Tolerance calculators."""

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
