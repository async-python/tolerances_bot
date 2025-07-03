"""Executor."""

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.dml import Insert, Update
from sqlalchemy.sql.selectable import Select


class Executor:
    """Executor class."""

    async def get_record(
        self: object,
        query: Select | Insert | Update,
        schema: type[BaseModel],
        session: AsyncSession,
    ) -> type[BaseModel] | None:
        """Get record with from db."""
        async with session.begin_nested():
            results = await session.execute(query)
        data = results.scalar_one_or_none()
        return schema.model_validate(data) if data else None

    async def get_record_relationship(
        self: object,
        query: Select | Insert | Update,
        schema: type[BaseModel],
        session: AsyncSession,
    ) -> BaseModel | None:
        """Get record with relationship from db."""
        async with session.begin_nested():
            results = await session.execute(query)
        data = results.unique().scalar_one_or_none()
        return schema.model_validate(data) if data else None

    async def get_records(
        self: object,
        query: Select | Insert | Update,
        schema: type[BaseModel],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Get records with from db."""
        async with session.begin_nested():
            results = await session.execute(query)
        data = results.scalars()
        return [schema.model_validate(row) for row in data]

    async def get_records_relationship(
        self: object,
        query: Select | Insert | Update,
        schema: type[BaseModel],
        session: AsyncSession,
    ) -> list[BaseModel]:
        """Get records with relationship from db."""
        async with session.begin_nested():
            results = await session.execute(query)
        data = results.unique().scalars().all()
        return [schema.model_validate(row) for row in data]
