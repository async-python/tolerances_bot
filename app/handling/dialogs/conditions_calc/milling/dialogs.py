"""Conditions milling calculator dialog module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.conditions_calc.milling.getters import (
    get_data_milling_window_1,
    get_data_milling_window_2,
    get_data_milling_window_3,
    get_data_milling_window_4,
    get_data_milling_window_5,
    get_data_milling_window_6,
)
from app.handling.dialogs.conditions_calc.milling.handlers import (
    go_window_1,
    go_window_2,
    go_window_3,
    go_window_4,
    go_window_5,
    go_window_6,
    go_next,
    go_back,
    go_quit,
    on_diameter_received,
    on_cutting_speed_received,
    on_teeth_number_received,
    on_feed_per_tooth_received,
    on_spindle_speed_received,
    on_feed_rate_received,
    go_return,
)

from app.handling.states.conditions_calc import ConditionsMillingSG

CONDITIONS_FORMAT = Format(
    "{tool_diameter} \n {cutting_speed} \n {spindle_speed} "
    "\n {number_of_teeth} \n {feed_per_tooth} \n {feed_rate}"
)

conditions_milling_dialog = Dialog(
    Window(  # Window 1
        CONDITIONS_FORMAT,
        Format("{window_1_greeting}"),
        MessageInput(on_diameter_received),
        Row(
            Button(Format("🔹 {Button_1}"), id="b_first"),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
            Button(Format("{Button_6}"), id="b_sixth", on_click=go_window_6),
        ),
        Row(
            Button(
                Format("{button_return}"), id="b_return", on_click=go_return
            ),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_milling_window_1,
        state=ConditionsMillingSG.window_1,
    ),
    Window(  # Window 2
        CONDITIONS_FORMAT,
        Format("{window_2_greeting}"),
        MessageInput(on_cutting_speed_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("🔹 {Button_2}"), id="b_second"),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
            Button(Format("{Button_6}"), id="b_sixth", on_click=go_window_6),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_milling_window_2,
        state=ConditionsMillingSG.window_2,
    ),
    Window(  # Window 3
        CONDITIONS_FORMAT,
        Format("{window_3_greeting}"),
        MessageInput(on_spindle_speed_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("🔹 {Button_3}"), id="b_third"),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
            Button(Format("{Button_6}"), id="b_sixth", on_click=go_window_6),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_milling_window_3,
        state=ConditionsMillingSG.window_3,
    ),
    Window(  # Window 4
        CONDITIONS_FORMAT,
        Format("{window_4_greeting}"),
        MessageInput(on_teeth_number_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("🔹 {Button_4}"), id="b_fourth"),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
            Button(Format("{Button_6}"), id="b_sixth", on_click=go_window_6),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_milling_window_4,
        state=ConditionsMillingSG.window_4,
    ),
    Window(  # Window 5
        CONDITIONS_FORMAT,
        Format("{window_5_greeting}"),
        MessageInput(on_feed_per_tooth_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("🔹 {Button_5}"), id="b_fifth"),
            Button(Format("{Button_6}"), id="b_sixth", on_click=go_window_6),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_milling_window_5,
        state=ConditionsMillingSG.window_5,
    ),
    Window(  # Window 6
        CONDITIONS_FORMAT,
        Format("{window_6_greeting}"),
        MessageInput(on_feed_rate_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
            Button(Format("🔹 {Button_6}"), id="b_sixth"),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_cancel}"), id="b_quit", on_click=go_quit),
        ),
        getter=get_data_milling_window_6,
        state=ConditionsMillingSG.window_6,
    ),
)
