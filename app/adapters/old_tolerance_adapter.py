"""Old Tolerance Adapter module."""

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.main_repository import repository

if TYPE_CHECKING:
    from app.schemas import OldToleranceRepoRelatedSchema


class OldToleranceAdapter:
    """Old Tolerance Adapter class."""

    @staticmethod
    async def get_old_tolerance_related_tolerance(
        name: str,
        session: AsyncSession,
    ) -> type["OldToleranceRepoRelatedSchema"] | None:
        """Returns tolerance data from db."""
        response = (
            await repository.old_tolerance.get_old_tolerance_related_tolerance(
                name=name,
                session=session,
            )
        )
        return response
