"""App configuration."""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class AppSettings(BaseSettings):
    """App settings."""

    DEBUG: bool
    BOT_TOKEN: str

    model_config = SettingsConfigDict(env_prefix="APP_")

class RedisSettings(BaseSettings):
    REDIS_PASSWORD: str
    REDIS_PORT: int
    REDIS_HOST: str
    REDIS_DB: int
    REDIS_POOL_SIZE: int
    REDIS_CONNECT_TIMEOUT: int

    model_config = SettingsConfigDict(env_prefix="DBR_")

    @property
    def get_redis_url(self: type[BaseSettings]) -> str:
        """Return database url."""
        return (
            f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}"
            f":{self.REDIS_PORT}/{self.REDIS_DB}"
        )

class DatabaseSettings(BaseSettings):
    """Database settings."""

    DRIVER: str
    USER: str
    PASSWORD: str
    DB_NAME: str
    HOST: str
    PORT: str

    model_config = SettingsConfigDict(env_prefix="DB_")

    @property
    def get_db_url(self: type[BaseSettings]) -> str:
        """Return database url."""
        return (
            f"{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}"
            f":{self.PORT}/{self.DB_NAME}"
        )


class Config(BaseException):
    """Common config."""

    APP: AppSettings = AppSettings()
    DB: DatabaseSettings = DatabaseSettings()
    DBR: RedisSettings = RedisSettings()


CONFIG = Config()
