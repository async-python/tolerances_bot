"""Start state module."""

from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    """Start state class."""

    start = State()
