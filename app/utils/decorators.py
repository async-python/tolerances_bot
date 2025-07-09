"""Decorators."""

from collections.abc import Coroutine, Callable
from functools import wraps
from typing import Any


def inject_resources(
    handler: Callable,
) -> Callable[
    [tuple[Any, ...], dict[str, dict]], Coroutine[Any, Any, Coroutine]
]:
    """Inject translator_runner and session to any handler."""

    @wraps(handler)
    async def wrapper(
        *args: Any,
        **kwargs: dict,
    ) -> Coroutine:
        """Adds translator_runner and session to handler."""
        dialog_manager = args[2]
        i18n = dialog_manager.middleware_data.get("i18n")
        session = dialog_manager.middleware_data.get("session")
        return await handler(
            *args,
            **kwargs,
            i18n=i18n,
            session=session,
        )

    return wrapper
