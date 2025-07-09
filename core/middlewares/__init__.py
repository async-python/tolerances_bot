from aiogram import Dispatcher

from .i18n import TranslatorRunnerMiddleware
from .session import DbSessionMiddleware
from ..database import db_pool_context


def setup_middlewares(dp: Dispatcher):
    dp.update.outer_middleware(DbSessionMiddleware(db_pool_context))
    dp.update.middleware(TranslatorRunnerMiddleware())
