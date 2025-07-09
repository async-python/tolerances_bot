"""Start dialog handlers module."""

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.handling.states.conditions_calc import ConditionsStartSG
from app.handling.states.find_tolerance import FindToleranceSG
from app.handling.states.map_tolerance import MapToleranceSG


async def button_start_find_tolerance_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Starts find tolerance dialog."""
    return await dialog_manager.start(state=FindToleranceSG.start)


async def button_start_map_tolerance_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Starts mapping tolerance dialog."""
    return await dialog_manager.start(state=MapToleranceSG.start)


async def button_start_calc_conditions_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Starts conditions dialog."""
    return await dialog_manager.start(state=ConditionsStartSG.start)
