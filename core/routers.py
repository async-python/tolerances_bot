"""Bot routers module."""

from aiogram import Dispatcher

from app.handling.dialogs.conditions_calc.conditions_start.dialogs import (
    conditions_start_dialog,
)
from app.handling.dialogs.conditions_calc.drilling.dialogs import (
    conditions_drilling_dialog,
)
from app.handling.dialogs.conditions_calc.milling.dialogs import (
    conditions_milling_dialog,
)
from app.handling.dialogs.conditions_calc.turning.dialogs import (
    conditions_turning_dialog,
)
from app.handling.dialogs.find_tolerance.dialogs import find_tolerance_dialog
from app.handling.dialogs.old_tolerance.dialogs import map_tolerance_dialog
from app.handling.dialogs.start.dialogs import start_dialog
from app.handling.handlers.commands import commands_router


def setup_routers(dp: Dispatcher) -> None:
    """Include all necessary routers."""
    dp.include_router(commands_router)
    dp.include_routers(
        start_dialog,
        find_tolerance_dialog,
        map_tolerance_dialog,
        conditions_start_dialog,
        conditions_milling_dialog,
        conditions_drilling_dialog,
        conditions_turning_dialog,
    )
