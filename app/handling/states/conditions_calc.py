"""Conditions calculator state module."""

from aiogram.fsm.state import State, StatesGroup


class ConditionsStartSG(StatesGroup):
    """Conditions calculator start state class."""

    start = State()


class ConditionsMillingSG(StatesGroup):
    """Conditions calculator milling state class."""

    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()
    window_5 = State()
    window_6 = State()


class ConditionsTurningSG(StatesGroup):
    """Conditions calculator turning state class."""

    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()
    window_5 = State()


class ConditionsDrillingSG(StatesGroup):
    """Conditions calculator drilling state class."""

    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()
    window_5 = State()
