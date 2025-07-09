"""App main module."""

import asyncio

from aiogram import Dispatcher

from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from core.middlewares import setup_middlewares
from app.utils.i18n import create_translator_hub
from core.exceptions.exception_handlers import register_exception_handlers
from core.logger import init_logging
from core.redis.redis_storage import create_redis_storage
from core.routers import setup_routers
from core.telegram_bot import create_bot


async def start_bot() -> None:
    """Configure and start the bot."""
    init_logging()
    translator_hub: TranslatorHub = create_translator_hub()
    fsm_storage = create_redis_storage()
    bot = create_bot()

    dp = Dispatcher(storage=fsm_storage)
    register_exception_handlers(dp)
    setup_middlewares(dp)
    setup_routers(dp)
    setup_dialogs(dp)

    await dp.start_polling(
        bot,
        _translator_hub=translator_hub,
    )


if __name__ == "__main__":
    asyncio.run(start_bot())
