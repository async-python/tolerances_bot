"""Commands handlers module."""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.handling.states.start import StartSG

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    dialog_manager: DialogManager,
) -> None:
    """Command Start handler."""
    return await dialog_manager.start(
        state=StartSG.start, mode=StartMode.RESET_STACK
    )
