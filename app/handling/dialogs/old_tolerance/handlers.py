"""Find tolerance dialog handlers."""

from typing import TYPE_CHECKING
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.old_tolerance_adapter import OldToleranceAdapter
from app.controllers.old_tolerance_controller import OldToleranceController
from app.handling.states.start import StartSG
from app.utils.decorators import inject_resources

if TYPE_CHECKING:
    from app.schemas import OldToleranceRepoRelatedSchema
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
    old_tolerance: (
        type[OldToleranceRepoRelatedSchema] | None
    ) = await OldToleranceAdapter.get_old_tolerance_related_tolerance(
        name=message.text,
        session=session,
    )
    related_tolerances_list: str = (
        await OldToleranceController.process_and_validate_related_tolerances(
            old_tolerance=old_tolerance,
            i18n=i18n,
        )
    )
    await message.answer(
        i18n.old.tolerance.found_text(list=related_tolerances_list)
    )
    return await dialog_manager.next()


async def on_button_continue_clicked(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    """Return back window."""
    return await dialog_manager.back()


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
