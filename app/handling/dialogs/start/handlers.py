"""Start dialog handlers module."""

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.handling.states.find_tolerance import FindToleranceSG
from app.handling.states.map_tolerance import MapToleranceSG


async def button_start_find_tolerance_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Change dialog to find tolerance handler."""
    await dialog_manager.start(state=FindToleranceSG.start)


async def button_start_map_tolerance_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Change dialog to find tolerance handler."""
    await dialog_manager.start(state=MapToleranceSG.start)
