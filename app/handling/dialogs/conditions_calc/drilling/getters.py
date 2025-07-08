from typing import TYPE_CHECKING

from app.utils.dialog_getters import get_data_window_generic

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner

BUTTONS = {
    "Button_1": "D",
    "Button_2": "Vc",
    "Button_3": "n",
    "Button_4": "fn",
    "Button_5": "Vf",
}

FIELD_MAP = {
    "tool_diameter": lambda i18n,
    val: i18n.conditions.milling.tool_diameter.text(value=val),
    "cutting_speed": lambda i18n,
    val: i18n.conditions.milling.cutting_speed.text(value=val),
    "spindle_speed": lambda i18n,
    val: i18n.conditions.milling.spindle_speed.text(value=val),
    "feed_per_tooth": lambda i18n,
    val: i18n.conditions.common.feed_per_rev.text(value=val),
    "feed_rate": lambda i18n, val: i18n.conditions.milling.feed_rate.text(
        value=val
    ),
}


def turning_feed_per_rev_prompt(i18n: "TranslatorRunner") -> str:
    return i18n.conditions.prompt.feed_per_rev.text()


async def get_data_drilling_window_1(*args, **kwargs):
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="tool_diameter",
        window_greeting_key="window_1_greeting",
        data_key="drilling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_drilling_window_2(*args, **kwargs):
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="cutting_speed",
        window_greeting_key="window_2_greeting",
        data_key="drilling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_drilling_window_3(*args, **kwargs):
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="spindle_speed",
        window_greeting_key="window_3_greeting",
        data_key="drilling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_drilling_window_4(*args, **kwargs):
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_per_tooth",
        window_greeting_key="window_4_greeting",
        data_key="drilling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
        window_greeting_getter=turning_feed_per_rev_prompt,
    )


async def get_data_drilling_window_5(*args, **kwargs):
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_rate",
        window_greeting_key="window_5_greeting",
        data_key="drilling",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )
