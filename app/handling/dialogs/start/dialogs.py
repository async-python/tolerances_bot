"""Start dialog routers module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.start.getters import get_hello
from app.handling.dialogs.start.handlers import (
    button_start_find_tolerance_click,
    button_start_map_tolerance_click,
    button_start_calc_conditions_click,
)
from app.handling.states.start import StartSG

start_dialog = Dialog(
    Window(
        Format("{hello_user}"),
        Button(
            Format("{button1}"),
            id="start_button1_pressed",
            on_click=button_start_find_tolerance_click,
        ),
        Button(
            Format("{button2}"),
            id="start_button2_pressed",
            on_click=button_start_map_tolerance_click,
        ),
        Button(
            Format("{button3}"),
            id="start_button3_pressed",
            on_click=button_start_calc_conditions_click,
        ),
        getter=get_hello,
        state=StartSG.start,
    ),
)
