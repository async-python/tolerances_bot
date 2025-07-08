"""Base app error."""

from core.exceptions.exception_schemas import ErrorMessage


class BaseAppError(Exception):
    """Base app error class."""

    def __init__(
        self: object,
        name: ErrorMessage | str,
    ) -> None:
        """Initialize a new base app error class."""
        self.name = name

    def __str__(self: object) -> str:
        """String representation of the error."""
        return self.name if isinstance(self.name, str) else self.name.message


class NotFoundError(BaseAppError):
    """Not found error class."""

    pass


class ConflictError(BaseAppError):
    """Conflict error class."""

    pass


class UnauthorizedError(BaseAppError):
    """Unauthorized error class."""

    pass


class ForbiddenError(BaseAppError):
    """Forbidden error class."""

    pass


class ValuePydanticError(BaseAppError):
    """Value pydantic error class."""

    pass


class BadRequestError(BaseAppError):
    """Bad request error class."""

    pass


class UnavailableServiceError(BaseAppError):
    """Unavailable service error class."""

    pass
