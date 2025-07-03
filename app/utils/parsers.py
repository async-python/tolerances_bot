"""Parsers module."""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner

from core.exceptions.base_exceptions import BadRequestError


async def parse_tolerance(
    input_row: str, i18n: "TranslatorRunner"
) -> tuple[float, str, int]:
    """Parse tolerance parameters from input row."""
    pattern = r"^(\d+(?:[.,]\d+)?)[ ]*([A-Za-z]+)[ ]*(\d+)$"
    match = re.match(pattern, input_row.strip())

    if not match:
        raise BadRequestError(
            name=i18n.messages.wrong_tolerance_format(name=input_row)
        )

    size_str = match.group(1).replace(",", ".")
    size = float(size_str)
    letter = match.group(2)
    quality = int(match.group(3))

    return size, letter, quality
