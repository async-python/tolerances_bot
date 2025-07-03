"""App main module."""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import DefaultKeyBuilder, Redis, RedisStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from app.handling.dialogs.find_tolerance.dialogs import find_tolerance_dialog
from app.handling.dialogs.start.dialogs import start_dialog
from app.handling.handlers.commands import commands_router
from app.middlewares.i18n import TranslatorRunnerMiddleware
from app.middlewares.session import DbSessionMiddleware
from app.utils.i18n import create_translator_hub
from core.config import CONFIG
from core.database import db_pool_context
from core.exceptions.exception_handlers import register_exception_handlers
from core.logger import init_logging


async def main() -> None:
    """Configure the bot."""
    init_logging()

    redis = Redis.from_url(
        url=CONFIG.APP.get_redis_url,
        decode_responses=True,
        max_connections=CONFIG.APP.REDIS_POOL_SIZE,
        socket_connect_timeout=CONFIG.APP.REDIS_CONNECT_TIMEOUT,
    )

    fsm_storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )

    bot = Bot(
        token=CONFIG.APP.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(
        storage=fsm_storage,
    )

    # process exceptions
    register_exception_handlers(dp)

    # register middlewares
    dp.update.outer_middleware(DbSessionMiddleware(db_pool_context))
    dp.update.middleware(TranslatorRunnerMiddleware())

    # include routers
    dp.include_router(commands_router)
    dp.include_routers(
        start_dialog,
        find_tolerance_dialog,
    )

    setup_dialogs(dp)
    translator_hub: TranslatorHub = create_translator_hub()

    bot_representation = await bot.me()
    logging.info(
        f"Bot {bot_representation.first_name} is ready to serve requests"
    )
    await dp.start_polling(
        bot,
        _translator_hub=translator_hub,
    )


if __name__ == "__main__":
    asyncio.run(main())
