"""Old Tolerance repository."""

from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import OldTolerance
from app.schemas import OldToleranceRepoSchema, OldToleranceRepoRelatedSchema
from core.database import Executor


class OldToleranceRepository(Executor):
    """Old Tolerance repository class."""

    async def create_tolerance(
        self: type[Executor],
        data: dict,
        session: AsyncSession,
    ) -> OldToleranceRepoSchema | None:
        """Create Old Tolerance in database function."""
        query = insert(OldTolerance).values(**data).returning(OldTolerance)
        return await self.get_record(
            query=query,
            schema=OldToleranceRepoSchema,
            session=session,
        )

    async def create_tolerance_bulk(
        self: type[Executor],
        data: list[dict],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Create Old Tolerance bulk in database function."""
        query = insert(OldTolerance).values(data).returning(OldTolerance)
        return await self.get_records(
            query=query,
            schema=OldToleranceRepoSchema,
            session=session,
        )

    async def get_old_tolerance_related_tolerance(
        self: type[Executor],
        name: str,
        session: AsyncSession,
    ) -> type["OldToleranceRepoRelatedSchema"] | None:
        """Get from db old tolerance with related tolerances."""
        query = select(OldTolerance).where(OldTolerance.name == name)
        return await self.get_record_relationship(
            query=query,
            schema=OldToleranceRepoRelatedSchema,
            session=session,
        )
