"""Map tolerance state module."""

from aiogram.fsm.state import State, StatesGroup


class MapToleranceSG(StatesGroup):
    """Map tolerance state class."""

    start = State()
    second = State()
