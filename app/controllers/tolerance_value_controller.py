"""Tolerance Value Controller module."""

from typing import TYPE_CHECKING

from core.exceptions.error_classes.tolerance_value import (
    ToleranceValueException,
)

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import ToleranceValueRepoSchema


class ToleranceValueController:
    """Tolerance Value Controller class."""

    @classmethod
    async def validate_tolerance_value(
        cls: object,
        tolerance_value: type["ToleranceValueRepoSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Validate tolerance values exists."""
        await ToleranceValueException.raise_exception_if_not_found(
            tolerance_value=tolerance_value,
            i18n=i18n,
        )
        return True
