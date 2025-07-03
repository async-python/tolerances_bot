"""Tolerance match repository."""

from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ToleranceMatch
from app.schemas import ToleranceMatchRepoSchema
from core.database import Executor


class ToleranceMatchRepository(Executor):
    """Tolerance match repository class."""

    async def create_tolerance_match(
        self: type[Executor],
        data: dict,
        session: AsyncSession,
    ) -> ToleranceMatchRepoSchema | None:
        """Create Tolerance in database function."""
        query = insert(ToleranceMatch).values(**data).returning(ToleranceMatch)
        return await self.get_record(
            query=query,
            schema=ToleranceMatchRepoSchema,
            session=session,
        )

    async def create_tolerance_match_bulk(
        self: type[Executor],
        data: list[dict],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Create Tolerance match bulk in database function."""
        query = insert(ToleranceMatch).values(data).returning(ToleranceMatch)
        return await self.get_records(
            query=query,
            schema=ToleranceMatchRepoSchema,
            session=session,
        )
