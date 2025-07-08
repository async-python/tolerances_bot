"""Conditions start getters module."""

from typing import TYPE_CHECKING
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


async def get_first_window_info(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for second window."""
    return {
        "first_message": i18n.conditions.start.prompt(),
        "next_step_milling": i18n.conditions.start.button.milling(),
        "next_step_turning": i18n.conditions.start.button.turning(),
        "next_step_drilling": i18n.conditions.start.button.drilling(),
        "return_prev": i18n.transition.button.return_prev(),
    }
