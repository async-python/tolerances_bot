"""Milling calculation getters."""

from typing import Any

from app.utils.dialog_getters import get_data_window_generic

BUTTONS = {
    "Button_1": "D",
    "Button_2": "Vc",
    "Button_3": "n",
    "Button_4": "Z",
    "Button_5": "fz",
    "Button_6": "Vf",
}

FIELD_MAP = {
    "tool_diameter": lambda i18n,
    val: i18n.conditions.common.tool_diameter.text(value=val),
    "cutting_speed": lambda i18n,
    val: i18n.conditions.common.cutting_speed.text(value=val),
    "spindle_speed": lambda i18n,
    val: i18n.conditions.common.spindle_speed.text(value=val),
    "number_of_teeth": lambda i18n,
    val: i18n.conditions.common.number_of_teeth.text(value=val),
    "feed_per_tooth": lambda i18n,
    val: i18n.conditions.common.feed_per_tooth.text(value=val),
    "feed_rate": lambda i18n, val: i18n.conditions.common.feed_rate.text(
        value=val
    ),
}


async def get_data_milling_window_1(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for tool diameter window 1."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="tool_diameter",
        window_greeting_key="window_1_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_milling_window_2(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for cutting speed window 2."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="cutting_speed",
        window_greeting_key="window_2_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_milling_window_3(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for spindle speed window 3."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="spindle_speed",
        window_greeting_key="window_3_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_milling_window_4(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for number of teeth window 4."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="number_of_teeth",
        window_greeting_key="window_4_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_milling_window_5(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for feed per tooth window 5."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_per_tooth",
        window_greeting_key="window_5_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_milling_window_6(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter for feed rate window 6."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_rate",
        window_greeting_key="window_6_greeting",
        data_key="milling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )
