"""Pydantic error constants."""

from core.exceptions.exception_schemas import ErrorMessage

UNEXPECTED_ERROR = ErrorMessage(
    message="Sorry, something went wrong, please try again later.",
    code_error="unexpectedError",
)
