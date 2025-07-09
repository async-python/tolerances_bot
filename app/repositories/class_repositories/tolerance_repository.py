"""Tolerance repository."""

from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Tolerance
from app.schemas import ToleranceRepoRelatedRangesSchema, ToleranceRepoSchema
from core.database import Executor


class ToleranceRepository(Executor):
    """Tolerance repository class."""

    async def create_tolerance(
        self: type[Executor],
        values: dict,
        session: AsyncSession,
    ) -> ToleranceRepoSchema | None:
        """Create Tolerance in database function."""
        query = insert(Tolerance).values(**values).returning(Tolerance)
        return await self.get_record(
            query=query,
            schema=ToleranceRepoSchema,
            session=session,
        )

    async def create_tolerance_bulk(
        self: type[Executor],
        data: list[dict],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Create Tolerance bulk in database function."""
        query = insert(Tolerance).values(data).returning(Tolerance)
        return await self.get_records(
            query=query,
            schema=ToleranceRepoSchema,
            session=session,
        )

    async def get_tolerance(
        self: type[Executor],
        letter: str,
        digit: int,
        session: AsyncSession,
    ) -> BaseModel | None:
        """Get tolerance from database function."""
        query = select(Tolerance).where(
            Tolerance.iso_digit == digit,
            Tolerance.iso_letter == letter,
        )
        return await self.get_record(
            query=query,
            schema=ToleranceRepoSchema,
            session=session,
        )

    async def get_tolerance_related_ranges(
        self: type[Executor],
        letter: str,
        digit: int,
        session: AsyncSession,
    ) -> ToleranceRepoRelatedRangesSchema | None:
        """Get tolerance with related ranges from database function."""
        query = (
            select(Tolerance)
            .options(joinedload(Tolerance.linked_ranges))
            .where(
                Tolerance.iso_digit == digit,
                Tolerance.iso_letter == letter,
            )
        )
        return await self.get_record_relationship(
            query=query,
            schema=ToleranceRepoRelatedRangesSchema,
            session=session,
        )
