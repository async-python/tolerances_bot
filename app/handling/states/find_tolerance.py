"""Find tolerance state module."""

from aiogram.fsm.state import State, StatesGroup


class FindToleranceSG(StatesGroup):
    """Find tolerance state class."""

    start = State()
    second = State()
