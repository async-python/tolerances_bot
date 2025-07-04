"""Find tolerance getters module."""

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
    """Getter for first window."""
    return {
        "map_answer": i18n.map.tolerance.invite_text(),
    }


async def get_second_window_info(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for second window."""
    return {
        "next_step": i18n.next.step(),
        "continue_step": i18n.ContinueAction.step(),
        "back_step": i18n.back.step(),
    }
