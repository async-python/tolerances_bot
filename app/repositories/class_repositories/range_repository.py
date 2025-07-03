"""Range repository."""

from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Range
from app.schemas import RangeRepoSchema
from core.database import Executor


class RangeRepository(Executor):
    """Range repository class."""

    async def create_range(
        self: type[Executor],
        data: dict,
        session: AsyncSession,
    ) -> RangeRepoSchema | None:
        """Create Range in database function."""
        query = insert(Range).values(**data).returning(Range)
        return await self.get_record(
            query=query,
            schema=RangeRepoSchema,
            session=session,
        )

    async def create_range_bulk(
        self: type[Executor],
        data: list[dict],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Create Range bulk in database function."""
        query = insert(Range).values(data).returning(Range)
        return await self.get_records(
            query=query,
            schema=RangeRepoSchema,
            session=session,
        )
