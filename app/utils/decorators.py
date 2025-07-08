"""Decorators."""

from collections.abc import Coroutine, Callable
from functools import wraps
from typing import Any


def inject_resources(handler: Callable) -> Coroutine:
    """Inject translator_runner and session to any handler."""

    @wraps(handler)
    async def wrapper(
        *args: Any,
        **kwargs: dict,
    ) -> Coroutine:
        """Adds translator_runner and session to handler."""
        _, _, dialog_manager = args
        i18n = dialog_manager.middleware_data.get("i18n")
        session = dialog_manager.middleware_data.get("session")
        return await handler(
            *args,
            **kwargs,
            i18n=i18n,
            session=session,
        )

    return wrapper
