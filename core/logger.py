"""Init loguru."""

import logging
import sys
from pprint import pformat

from loguru import logger
from loguru._defaults import LOGURU_FORMAT


class InterceptHandler(logging.Handler):
    """Intercept handler class."""

    def emit(self: object, record: logging.LogRecord) -> None:
        """Emits the record."""
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def format_record(record: dict) -> str:
    """Format a record."""
    format_string = LOGURU_FORMAT
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"],
            indent=4,
            compact=True,
            width=88,
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string


def init_logging() -> None:
    """Configure logging to use loguru."""
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.DEBUG)

    for name in logging.root.manager.loggerDict:
        logging.getLogger(name).handlers = []

    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "level": logging.DEBUG,
                "format": format_record,
            },
        ],
    )
