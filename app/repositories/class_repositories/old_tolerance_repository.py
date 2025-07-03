"""Old Tolerance repository."""

from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import OldTolerance
from app.schemas import OldToleranceRepoSchema
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
