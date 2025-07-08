"""Tolerance value exceptions."""

from typing import TYPE_CHECKING

from core.exceptions.base_exceptions import NotFoundError

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner
    from app.schemas import ToleranceValueRepoSchema


class ToleranceValueException:
    """Tolerance value exception class."""

    @staticmethod
    async def raise_exception_if_not_found(
        tolerance_value: type["ToleranceValueRepoSchema"] | None,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if wrong tolerance deviations."""
        if (
            not tolerance_value
            or tolerance_value.upper_value is None
            or tolerance_value.lower_value is None
        ):
            raise NotFoundError(name=i18n.messages.deviation_unavailable())
        return True
