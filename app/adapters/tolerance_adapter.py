"""Tolerance Adapter module."""

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.main_repository import repository
from app.utils.parsers import parse_tolerance

if TYPE_CHECKING:
    from app.schemas import ToleranceRepoRelatedRangesSchema
    from app.locales.stub import TranslatorRunner


class ToleranceAdapter:
    """Tolerance Adapter class."""

    @staticmethod
    async def get_parsed_tolerance(
        text: str,
        i18n: "TranslatorRunner",
        session: AsyncSession,
    ) -> tuple[Decimal, type["ToleranceRepoRelatedRangesSchema"] | None]:
        """Returns tolerance data from db."""
        target_value, letter, quality = await parse_tolerance(text, i18n)
        response = await repository.tolerance.get_tolerance_related_ranges(
            letter=letter,
            digit=quality,
            session=session,
        )
        return target_value, response
