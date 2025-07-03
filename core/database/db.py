"""Database connection and sessions."""

import typing as t
from contextlib import asynccontextmanager

from loguru import logger
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from core.config import CONFIG
from core.exceptions.base_exceptions import ConflictError

DATABASE_URL = CONFIG.DB.get_db_url
engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    poolclass=NullPool,
    echo=CONFIG.APP.DEBUG,
    pool_recycle=3600,
)


async def get_session() -> t.AsyncGenerator:
    """Returns a session from pool sessions."""
    try:
        async_session = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        async with async_session() as session, session.begin():
            yield session
    except exc.SQLAlchemyError as error:
        await session.rollback()
        logger.error(error._message())
        raise ConflictError(name=error._message())
    except Exception as error:
        logger.error(error)
        raise


db_pool_context = asynccontextmanager(get_session)
