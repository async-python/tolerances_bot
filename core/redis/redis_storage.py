"""Redis storage."""

from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from core.config import CONFIG


def create_redis_storage() -> RedisStorage:
    """Returns redis storage instance."""
    redis = Redis.from_url(
        url=CONFIG.DBR.get_redis_url,
        decode_responses=True,
        max_connections=CONFIG.DBR.REDIS_POOL_SIZE,
        socket_connect_timeout=CONFIG.DBR.REDIS_CONNECT_TIMEOUT,
    )
    return RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )
