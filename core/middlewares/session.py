"""Session Middleware."""

from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker


class DbSessionMiddleware(BaseMiddleware):
    """Session Middleware Class."""

    def __init__(self, session_pool: async_sessionmaker) -> None:
        """Initialize the middleware."""
        super().__init__()
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        """Addition a session to data."""
        async with self.session_pool() as session:
            data["session"] = session
            return await handler(event, data)
