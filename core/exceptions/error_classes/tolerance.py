"""Tolerance exceptions."""

from typing import TYPE_CHECKING

from core.exceptions.base_exceptions import NotFoundError

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import ToleranceRepoRelatedRangesSchema


class ToleranceException:
    """Tolerance Exception class."""

    @staticmethod
    async def raise_exception_if_not_found(
        tolerance: type["ToleranceRepoRelatedRangesSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if not found."""
        if not tolerance:
            raise NotFoundError(name=i18n.messages.tolerance_unavailable())
        return True
