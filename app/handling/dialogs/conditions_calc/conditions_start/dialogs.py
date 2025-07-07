"""Conditions start dialog module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.conditions_calc.conditions_start.getters import (
    get_first_window_info,
)
from app.handling.dialogs.conditions_calc.conditions_start.handlers import (
    on_button_mill_clicked,
    on_button_turning_clicked,
    on_button_drilling_clicked,
    on_button_return_clicked,
)
from app.handling.states.conditions_calc import ConditionsStartSG


conditions_start_dialog = Dialog(
    Window(
        Format(
            "{first_message}",
        ),
        Row(
            Button(
                text=Format("{next_step_milling}"),
                id="conditions_calc_button_1",
                on_click=on_button_mill_clicked,
            ),
            Button(
                text=Format("{next_step_drilling}"),
                id="conditions_calc_button_2",
                on_click=on_button_drilling_clicked,
            ),
            Button(
                text=Format("{next_step_turning}"),
                id="conditions_calc_button_3",
                on_click=on_button_turning_clicked,
            ),
        ),
        Button(
            text=Format("{back_step}"),
            id="conditions_calc_button_back",
            on_click=on_button_return_clicked,
        ),
        getter=get_first_window_info,
        state=ConditionsStartSG.start,
    ),
)
