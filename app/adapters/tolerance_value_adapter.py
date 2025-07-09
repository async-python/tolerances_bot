"""Tolerance Value Adapter module."""

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.main_repository import repository

if TYPE_CHECKING:
    from app.schemas import ToleranceValueRepoSchema


class ToleranceValueAdapter:
    """Tolerance Value Adapter class."""

    @staticmethod
    async def get_tolerance_value(
        target_value: Decimal,
        tolerance_id: UUID,
        range_ids: list[UUID],
        session: AsyncSession,
    ) -> type["ToleranceValueRepoSchema"] | None:
        """Returns tolerance value data from db."""
        return await repository.tolerance_value.get_tolerance_value(
            target_value=target_value,
            tolerance_id=tolerance_id,
            range_ids=range_ids,
            session=session,
        )
