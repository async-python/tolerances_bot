"""Find tolerance dialog handlers."""

from typing import TYPE_CHECKING
from uuid import UUID

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.tolerance_adapter import ToleranceAdapter
from app.adapters.tolerance_value_adapter import ToleranceValueAdapter
from app.controllers.range_controller import RangeController
from app.controllers.tolerance_controller import ToleranceController
from app.controllers.tolerance_value_controller import ToleranceValueController
from app.handling.states.start import StartSG
from app.utils.calculators import calculate_deviations_localized
from app.utils.decorators import inject_resources

if TYPE_CHECKING:
    from app.schemas import ToleranceValueRepoSchema
    from app.locales.stub import TranslatorRunner


@inject_resources
async def on_text_received(
    message: Message,
    message_input: MessageInput,
    dialog_manager: DialogManager,
    i18n: "TranslatorRunner",
    session: AsyncSession,
) -> None:
    """Handle user's input tolerance."""
    await dialog_manager.next()


async def on_button_continue_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Return back window."""
    await dialog_manager.back()


async def on_button_return_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Go to start window."""
    await dialog_manager.start(
        state=StartSG.start,
        mode=StartMode.RESET_STACK,
    )
