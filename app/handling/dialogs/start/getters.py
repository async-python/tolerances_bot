"""Start dialog getters module."""

from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


async def get_hello(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs: dict,
) -> dict[str, str]:
    """Start dialog data getter."""
    username = html.quote(event_from_user.full_name)
    return {
        "hello_user": i18n.dialog.start.prompt.text(username=username),
        "button1": i18n.dialog.start.button.tolerance(),
        "button2": i18n.dialog.start.button.old_tolerance(),
        "button3": i18n.dialog.start.button.conditions(),
    }
