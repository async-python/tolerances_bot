"""Conditions exceptions."""

from typing import TYPE_CHECKING

from core.exceptions.base_exceptions import BadRequestError

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


class ConditionsException:
    """Conditions exception class."""

    @staticmethod
    async def raise_exception_if_not_float(
        value: str,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if value is not float."""
        try:
            float(value.replace(",", "."))
        except ValueError:
            raise BadRequestError(
                name=i18n.messages.conditions.value_not_float()
            )
        return True

    @staticmethod
    async def raise_exception_if_not_int(
        value: str,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if value is not integer."""
        if not value.isdigit():
            raise BadRequestError(name=i18n.messages.conditions.value_not_int())
        return True

    @staticmethod
    async def raise_exception_if_zero_or_less(
        value: str,
        i18n: "TranslatorRunner",
    ) -> bool:
        """Raises an exception if value is zero or less."""
        if float(value.replace(",", ".")) <= 0:
            raise BadRequestError(name=i18n.messages.conditions.wrong_value())
        return True
