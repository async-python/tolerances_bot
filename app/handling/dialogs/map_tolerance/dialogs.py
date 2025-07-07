"""Map tolerance dialog module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.map_tolerance.getters import (
    get_first_window_info,
    get_second_window_info,
)
from app.handling.dialogs.map_tolerance.handlers import (
    on_text_received,
    on_button_continue_clicked,
    on_button_return_clicked,
)
from app.handling.states.map_tolerance import MapToleranceSG


map_tolerance_dialog = Dialog(
    Window(
        Format(
            "{map_answer}",
        ),
        MessageInput(on_text_received),  # noqa
        getter=get_first_window_info,
        state=MapToleranceSG.start,
    ),
    Window(
        Format(
            "{next_step}",
        ),
        Row(
            Button(
                text=Format("{continue_step}"),
                id="find_map_tol_button_1",
                on_click=on_button_continue_clicked,
            ),
            Button(
                text=Format("{back_step}"),
                id="find_map_tol_button_2",
                on_click=on_button_return_clicked,
            ),
        ),
        getter=get_second_window_info,
        state=MapToleranceSG.second,
    ),
)
