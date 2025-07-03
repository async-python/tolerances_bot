import logging
from aiogram import Router, F
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from loguru import logger

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


async def generic_error_handler(event: ErrorEvent):
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
    ExceptionTypeFilter(Exception), F.update.message.as_("message")
)
async def fallback_exception_handler(event: ErrorEvent):
    # logger.error(event.exception)
    logging.exception(event.exception)
    await event.update.message.answer(
        "🚨 Something went wrong. Please try later."
    )


def register_exception_handlers(dp):
    """Register the exception handlers."""
    dp.include_router(errors_router)
