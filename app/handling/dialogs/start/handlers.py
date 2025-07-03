"""Start dialog handlers module."""

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.handling.states.find_tolerance import FindToleranceSG


async def button_start_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Change dialog to find tolerance handler."""
    await dialog_manager.start(state=FindToleranceSG.start)
