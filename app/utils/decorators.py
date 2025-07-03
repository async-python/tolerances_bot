"""Decorators."""

from functools import wraps


def inject_resources(handler):
    """Inject translator_runner and session to any handler."""

    @wraps(handler)
    async def wrapper(*args, **kwargs):
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
