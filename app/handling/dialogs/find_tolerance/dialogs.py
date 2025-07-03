"""FInd tolerance dialog module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.find_tolerance.getters import (
    get_first_window_info,
    get_second_window_info,
)
from app.handling.dialogs.find_tolerance.handlers import (
    on_text_received,
    on_button_continue_clicked,
    on_button_return_clicked,
)
from app.handling.states.find_tolerance import FindToleranceSG


find_tolerance_dialog = Dialog(
    Window(
        Format(
            "{answer}",
        ),
        MessageInput(on_text_received),  # noqa
        getter=get_first_window_info,
        state=FindToleranceSG.start,
    ),
    Window(
        Format(
            "{next_step}",
        ),
        Row(
            Button(
                text=Format("{continue_step}"),
                id="find_tol_button_1",
                on_click=on_button_continue_clicked,
            ),
            Button(
                text=Format("{back_step}"),
                id="find_tol_button_2",
                on_click=on_button_return_clicked,
            ),
        ),
        getter=get_second_window_info,
        state=FindToleranceSG.second,
    ),
)
