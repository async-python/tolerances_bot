"""Range exceptions."""

from decimal import Decimal
from typing import TYPE_CHECKING

from core.exceptions.base_exceptions import NotFoundError

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import ToleranceRepoRelatedRangesSchema


class RangeException:
    """Range exceptions."""

    @staticmethod
    async def raise_exception_if_not_found(
        target_value: Decimal,
        tolerance: type["ToleranceRepoRelatedRangesSchema"],
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raise exception if range is not found."""
        if not len(tolerance.linked_ranges):
            raise NotFoundError(
                name=i18n.messages.dimension_unavailable(
                    target_value=target_value,
                ),
            )
        return True
