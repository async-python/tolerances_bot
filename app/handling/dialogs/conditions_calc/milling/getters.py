from typing import TYPE_CHECKING
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from app.handling.shemas.conditions import ConditionSchema

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner

PLUG = "__"
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
    val: i18n.conditions.milling.tool_diameter.text(value=val),
    "cutting_speed": lambda i18n,
    val: i18n.conditions.milling.cutting_speed.text(value=val),
    "spindle_speed": lambda i18n,
    val: i18n.conditions.milling.spindle_speed.text(value=val),
    "number_of_teeth": lambda i18n,
    val: i18n.conditions.milling.number_of_teeth.text(value=val),
    "feed_per_tooth": lambda i18n,
    val: i18n.conditions.milling.feed_per_tooth.text(value=val),
    "feed_rate": lambda i18n, val: i18n.conditions.milling.feed_rate.text(
        value=val
    ),
}


async def get_data_milling_window_generic(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    active_field: str,
    window_greeting_key: str,
    **kwargs: dict,
) -> dict[str, str]:
    """Universal getter for milling windows."""
    data = dialog_manager.dialog_data.get("milling", {})
    conditions = ConditionSchema(**data)

    result = {
        f"{window_greeting_key}": getattr(
            i18n.conditions.prompt, active_field
        ).text(),
        "button_forward": i18n.transition.button.forward(),
        "button_back": i18n.transition.button.back(),
        "button_cancel": i18n.transition.button.cancel(),
        "button_return": i18n.transition.button.return_prev(),
    }

    for field in FIELD_MAP.keys():
        value = getattr(conditions, field) or PLUG
        prefix = "->" if field == active_field else "--"
        result[field] = f"{prefix}{FIELD_MAP[field](i18n, value)}"

    result |= BUTTONS
    return result


async def get_data_milling_window_1(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="tool_diameter",
        window_greeting_key="window_1_greeting",
    )


async def get_data_milling_window_2(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="cutting_speed",
        window_greeting_key="window_2_greeting",
    )


async def get_data_milling_window_3(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="spindle_speed",
        window_greeting_key="window_3_greeting",
    )


async def get_data_milling_window_4(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="number_of_teeth",
        window_greeting_key="window_4_greeting",
    )


async def get_data_milling_window_5(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="feed_per_tooth",
        window_greeting_key="window_5_greeting",
    )


async def get_data_milling_window_6(*args, **kwargs):
    return await get_data_milling_window_generic(
        *args,
        **kwargs,
        active_field="feed_rate",
        window_greeting_key="window_6_greeting",
    )
