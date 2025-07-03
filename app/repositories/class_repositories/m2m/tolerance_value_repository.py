"""Tolerance value repository."""

from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Range, ToleranceValue
from app.schemas import ToleranceValueRepoSchema
from core.database import Executor


class ToleranceValueRepository(Executor):
    """Tolerance value repository class."""

    async def create_tolerance_value(
        self: type[Executor],
        data: dict,
        session: AsyncSession,
    ) -> ToleranceValueRepoSchema | None:
        """Create Tolerance in database function."""
        query = insert(ToleranceValue).values(**data).returning(ToleranceValue)
        return await self.get_record(
            query=query,
            schema=ToleranceValueRepoSchema,
            session=session,
        )

    async def create_tolerance_value_bulk(
        self: type[Executor],
        data: list[dict],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Create Tolerance value bulk in database function."""
        query = insert(ToleranceValue).values(data).returning(ToleranceValue)
        return await self.get_records(
            query=query,
            schema=ToleranceValueRepoSchema,
            session=session,
        )

    async def get_tolerance_value(
        self,
        target_value: int,
        tolerance_id: UUID,
        range_ids: list[UUID],
        session: AsyncSession,
    ) -> type[ToleranceValueRepoSchema] | None:
        """Get Tolerance value from database function."""
        query = (
            select(ToleranceValue)
            .join(Range, Range.id == ToleranceValue.range_id)
            .where(
                ToleranceValue.tolerance_id == tolerance_id,
                Range.id.in_(range_ids),
                Range.min_value < target_value,
                Range.max_value >= target_value,
            )
            .limit(1)
        )
        return await self.get_record(
            query=query,
            schema=ToleranceValueRepoSchema,
            session=session,
        )
