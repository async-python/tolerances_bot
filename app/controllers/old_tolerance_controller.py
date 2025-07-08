"""Old Tolerance Controller module."""

from typing import TYPE_CHECKING

from core.exceptions.error_classes.old_tolerance import OldToleranceException

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import OldToleranceRepoRelatedSchema


class OldToleranceController:
    """Old Tolerance Controller class."""

    @classmethod
    async def process_and_validate_related_tolerances(
        cls: object,
        old_tolerance: type["OldToleranceRepoRelatedSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> str:
        """Validate the old tolerance exists and related tolerances exists,
        returns list related tolerances in str."""
        await OldToleranceException.raise_exception_if_not_found(
            old_tolerance=old_tolerance,
            i18n=i18n,
        )
        await OldToleranceException.raise_exception_if_relations_not_found(
            old_tolerance=old_tolerance,
            i18n=i18n,
        )
        return ", ".join(
            [
                f"{x.iso_letter}{x.iso_digit}"
                for x in old_tolerance.linked_tolerances
            ]
        )
