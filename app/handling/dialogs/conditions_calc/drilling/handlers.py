"""Conditions drilling dialog handlers."""

from typing import TYPE_CHECKING
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.conditions_controller import (
    ConditionsController,
    ValueType,
)
from app.handling.states.conditions_calc import (
    ConditionsDrillingSG,
    ConditionsStartSG,
)
from app.handling.states.start import StartSG
from app.utils.decorators import inject_resources

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


async def on_start(
    start_data: dict,
    dialog_manager: DialogManager,
) -> None:
    """Add start data to common data."""
    dialog_manager.dialog_data.update(start_data)


async def _process_milling_conditions(
    message: Message,
    value_type: ValueType,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
) -> None:
    """Receives, process and saves drilling conditions."""
    data = dialog_manager.dialog_data.get("drilling")
    result = await ConditionsController.process_conditions(
        new_value=message.text,
        kind_of_value=value_type,
        conditions=data,
        i18n=i18n,
    )
    dialog_manager.dialog_data.update({"drilling": result.model_dump()})


@inject_resources
async def on_diameter_received(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Calculate drilling conditions if tool diameter changed."""
    await _process_milling_conditions(
        message=message,
        value_type=ValueType.DIAMETER,
        dialog_manager=dialog_manager,
        i18n=i18n,
    )
    await dialog_manager.next()


@inject_resources
async def on_cutting_speed_received(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Calculate drilling conditions if cutting speed changed."""
    await _process_milling_conditions(
        message=message,
        value_type=ValueType.CUTTING_SPEED,
        dialog_manager=dialog_manager,
        i18n=i18n,
    )
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_4)


@inject_resources
async def on_spindle_speed_received(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Calculate drilling conditions if spindle speed changed."""
    await _process_milling_conditions(
        message=message,
        value_type=ValueType.SPINDLE_SPEED,
        dialog_manager=dialog_manager,
        i18n=i18n,
    )
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_4)


@inject_resources
async def on_feed_per_rev(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Calculate drilling conditions if feed per tooth changed."""
    await _process_milling_conditions(
        message=message,
        value_type=ValueType.FEED_PER_TOOTH,
        dialog_manager=dialog_manager,
        i18n=i18n,
    )
    await dialog_manager.next()


@inject_resources
async def on_feed_rate_received(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Calculate drilling conditions if feed rate changed."""
    await _process_milling_conditions(
        message=message,
        value_type=ValueType.FEED_RATE,
        dialog_manager=dialog_manager,
        i18n=i18n,
    )


async def go_quit(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to previous window."""
    await dialog_manager.start(
        state=StartSG.start,
        mode=StartMode.RESET_STACK,
    )


async def go_back(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to previous window."""
    await dialog_manager.back()


async def go_next(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to next window."""
    await dialog_manager.next()


async def go_window_1(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to window 1."""
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_1)


async def go_window_2(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to window 2."""
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_2)


async def go_window_4(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to window 4."""
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_4)


async def go_window_3(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to window 3."""
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_3)


async def go_window_5(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Switch to window 5."""
    await dialog_manager.switch_to(state=ConditionsDrillingSG.window_5)


async def go_return(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Return to parent dialog."""
    await dialog_manager.start(
        state=ConditionsStartSG.start,
        mode=StartMode.RESET_STACK,
    )
