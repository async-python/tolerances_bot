"""Telegram bot module."""

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.config import CONFIG


def create_bot() -> Bot:
    """Creates bot instance."""
    return Bot(
        token=CONFIG.APP.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
