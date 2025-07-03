"""Tolerance Controller module."""

from typing import TYPE_CHECKING

from core.exceptions.error_classes.tolerance import ToleranceException

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import ToleranceRepoRelatedRangesSchema


class ToleranceController:
    """Controller for admin role management module class."""

    @classmethod
    async def validate_tolerance(
        cls: object,
        tolerance: type["ToleranceRepoRelatedRangesSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Validate role exists and one not super admin."""
        await ToleranceException.raise_exception_if_not_found(
            tolerance=tolerance,
            i18n=i18n,
        )
        return True
