"""Conditions drilling calculator dialog module."""

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from app.handling.dialogs.conditions_calc.drilling.getters import (
    get_data_drilling_window_1,
    get_data_drilling_window_2,
    get_data_drilling_window_3,
    get_data_drilling_window_4,
    get_data_drilling_window_5,
)
from app.handling.dialogs.conditions_calc.drilling.handlers import (
    go_window_1,
    go_window_2,
    go_window_3,
    go_window_4,
    go_window_5,
    go_next,
    go_back,
    go_quit,
    on_diameter_received,
    on_cutting_speed_received,
    on_feed_per_rev,
    on_spindle_speed_received,
    on_feed_rate_received,
    on_start,
    go_return,
)

from app.handling.states.conditions_calc import ConditionsDrillingSG

CONDITIONS_FORMAT = Format(
    "{tool_diameter} \n {cutting_speed} \n {spindle_speed} "
    "\n {feed_per_rev} \n {feed_rate}"
)

conditions_drilling_dialog = Dialog(
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
        ),
        Row(
            Button(
                Format("{button_return}"), id="b_return", on_click=go_return
            ),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_drilling_window_1,
        state=ConditionsDrillingSG.window_1,
    ),
    Window(  # Window 2
        CONDITIONS_FORMAT,
        Format("{window_2_greeting}"),
        MessageInput(on_cutting_speed_received),  # noqa
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("🔹 {Button_2}"), id="b_second"),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_drilling_window_2,
        state=ConditionsDrillingSG.window_2,
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
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_drilling_window_3,
        state=ConditionsDrillingSG.window_3,
    ),
    Window(  # Window 4
        CONDITIONS_FORMAT,
        Format("{window_4_greeting}"),
        MessageInput(on_feed_per_rev),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("🔹 {Button_4}"), id="b_fourth"),
            Button(Format("{Button_5}"), id="b_fifth", on_click=go_window_5),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_forward}"), id="b_next", on_click=go_next),
        ),
        getter=get_data_drilling_window_4,
        state=ConditionsDrillingSG.window_4,
    ),
    Window(  # Window 5
        CONDITIONS_FORMAT,
        Format("{window_5_greeting}"),
        MessageInput(on_feed_rate_received),
        Row(
            Button(Format("{Button_1}"), id="b_first", on_click=go_window_1),
            Button(Format("{Button_2}"), id="b_second", on_click=go_window_2),
            Button(Format("{Button_3}"), id="b_third", on_click=go_window_3),
            Button(Format("{Button_4}"), id="b_fourth", on_click=go_window_4),
            Button(Format("🔹 {Button_5}"), id="b_fifth"),
        ),
        Row(
            Button(Format("{button_back}"), id="b_back", on_click=go_back),
            Button(Format("{button_cancel}"), id="b_quit", on_click=go_quit),
        ),
        getter=get_data_drilling_window_5,
        state=ConditionsDrillingSG.window_5,
    ),
    on_start=on_start,
)
