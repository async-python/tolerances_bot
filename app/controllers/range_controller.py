"""Range Controller module."""

from typing import TYPE_CHECKING, List
from uuid import UUID

from core.exceptions.error_classes.range import RangeException

if TYPE_CHECKING:
    from app.schemas import ToleranceRepoRelatedRangesSchema
    from app.locales.stub import TranslatorRunner


class RangeController:
    """Controller for admin role management module class."""

    @classmethod
    async def process_and_validate_range_ids(
        cls: object,
        target_value: float,
        tolerance: type["ToleranceRepoRelatedRangesSchema"],
        i18n: "TranslatorRunner",
    ) -> list[UUID]:
        """Validate role exists and one not super admin."""
        await RangeException.raise_exception_if_not_found(
            target_value=target_value,
            tolerance=tolerance,
            i18n=i18n,
        )
        return [x.id for x in tolerance.linked_ranges]
