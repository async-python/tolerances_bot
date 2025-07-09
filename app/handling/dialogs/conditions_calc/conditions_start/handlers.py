"""Conditions start dialog handlers."""

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from app.handling.states.conditions_calc import (
    ConditionsMillingSG,
    ConditionsTurningSG,
    ConditionsDrillingSG,
)
from app.handling.states.start import StartSG


async def on_button_return_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Go to start window."""
    return await dialog_manager.start(
        state=StartSG.start,
        mode=StartMode.RESET_STACK,
    )


async def on_button_mill_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Go to milling conditions_calc dialog."""
    return await dialog_manager.start(
        state=ConditionsMillingSG.window_1,
    )


async def on_button_turning_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Go to turning conditions_calc dialog."""
    return await dialog_manager.start(
        state=ConditionsTurningSG.window_1,
        data={
            "turning": {
                "number_of_teeth": 1,
            }
        },
    )


async def on_button_drilling_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Go to drilling conditions_calc dialog."""
    return await dialog_manager.start(
        state=ConditionsDrillingSG.window_1,
        data={
            "drilling": {
                "number_of_teeth": 1,
            }
        },
    )
