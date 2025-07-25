"""Application exception handlers."""

import logging
from aiogram import Router, F, Dispatcher
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent

from core.exceptions.base_exceptions import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    UnauthorizedError,
    UnavailableServiceError,
    ValuePydanticError,
)

errors_router = Router()


async def generic_error_handler(event: ErrorEvent) -> None:
    """Outputs error message."""
    await event.update.message.answer(str(event.exception))


errors_router.error(ExceptionTypeFilter(NotFoundError))(generic_error_handler)
errors_router.error(ExceptionTypeFilter(ConflictError))(generic_error_handler)
errors_router.error(ExceptionTypeFilter(UnauthorizedError))(
    generic_error_handler
)
errors_router.error(ExceptionTypeFilter(ForbiddenError))(generic_error_handler)
errors_router.error(ExceptionTypeFilter(BadRequestError))(generic_error_handler)
errors_router.error(ExceptionTypeFilter(UnavailableServiceError))(
    generic_error_handler
)
errors_router.error(ExceptionTypeFilter(ValuePydanticError))(
    generic_error_handler
)


@errors_router.error(
    ExceptionTypeFilter(Exception),
    F.update.message.as_("message"),
)
async def fallback_exception_handler(event: ErrorEvent) -> None:
    """Common exception handler."""
    # logger.error(event.exception)
    logging.exception(event.exception)
    await event.update.message.answer(
        "🚨 Something went wrong. Please try later."
    )


def register_exception_handlers(
    dp: Dispatcher,
) -> None:
    """Register the exception handlers."""
    dp.include_router(errors_router)
