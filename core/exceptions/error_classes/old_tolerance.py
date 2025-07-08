"""Tolerance exceptions."""

from typing import TYPE_CHECKING

from core.exceptions.base_exceptions import NotFoundError

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import OldToleranceRepoRelatedSchema


class OldToleranceException:
    """Old Tolerance Exception class."""

    @staticmethod
    async def raise_exception_if_not_found(
        old_tolerance: type["OldToleranceRepoRelatedSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if not found."""
        if not old_tolerance:
            raise NotFoundError(name=i18n.messages.old_tolerance_unavailable())
        return True

    @staticmethod
    async def raise_exception_if_relations_not_found(
        old_tolerance: type["OldToleranceRepoRelatedSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if relations wasn't found."""
        if not old_tolerance.linked_tolerances:
            raise NotFoundError(
                name=i18n.messages.old_tolerance_relations_unavailable()
            )
        return True
