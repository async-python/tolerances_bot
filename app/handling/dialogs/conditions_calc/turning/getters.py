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
    "Button_4": "fn",
    "Button_5": "Vf",
}

FIELD_MAP = {
    "tool_diameter": lambda i18n,
    val: i18n.conditions.common.part_diameter.text(value=val),
    "cutting_speed": lambda i18n,
    val: i18n.conditions.milling.cutting_speed.text(value=val),
    "spindle_speed": lambda i18n,
    val: i18n.conditions.milling.spindle_speed.text(value=val),
    "feed_per_rev": lambda i18n, val: i18n.conditions.common.feed_per_rev.text(
        value=val
    ),
    "feed_rate": lambda i18n, val: i18n.conditions.milling.feed_rate.text(
        value=val
    ),
}


async def _get_conditions_from_dm(
    dialog_manager: DialogManager,
) -> ConditionSchema:
    data = dialog_manager.dialog_data.get("turning")
    return ConditionSchema(**data)


async def get_data_turning_window_generic(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    active_field: str,
    window_greeting_key: str,
    **kwargs,
) -> dict[str, str]:
    """Generic getter for turning windows."""
    conditions = await _get_conditions_from_dm(dialog_manager)

    result = {
        window_greeting_key: getattr(
            i18n.conditions.prompt, active_field if active_field != "tool_diameter" else "part_diameter"
        ).text(),
        "button_forward": i18n.transition.button.forward(),
        "button_back": i18n.transition.button.back(),
        "button_cancel": i18n.transition.button.cancel(),
        "button_return": i18n.transition.button.return_prev(),
    }

    for field, formatter in FIELD_MAP.items():
        val = (
            getattr(
                conditions,
                "feed_per_tooth" if field == "feed_per_rev" else field,
            )
            or PLUG
        )
        prefix = "->" if field == active_field else "--"
        result[field] = f"{prefix}{formatter(i18n, val)}"

    result |= BUTTONS
    return result


# === Тонкие обертки для Dialog ===


async def get_data_drilling_window_1(*args, **kwargs):
    return await get_data_turning_window_generic(
        *args,
        **kwargs,
        active_field="tool_diameter",
        window_greeting_key="window_1_greeting",
    )


async def get_data_drilling_window_2(*args, **kwargs):
    return await get_data_turning_window_generic(
        *args,
        **kwargs,
        active_field="cutting_speed",
        window_greeting_key="window_2_greeting",
    )


async def get_data_drilling_window_3(*args, **kwargs):
    return await get_data_turning_window_generic(
        *args,
        **kwargs,
        active_field="spindle_speed",
        window_greeting_key="window_3_greeting",
    )


async def get_data_drilling_window_4(*args, **kwargs):
    return await get_data_turning_window_generic(
        *args,
        **kwargs,
        active_field="feed_per_rev",
        window_greeting_key="window_4_greeting",
    )


async def get_data_drilling_window_5(*args, **kwargs):
    return await get_data_turning_window_generic(
        *args,
        **kwargs,
        active_field="feed_rate",
        window_greeting_key="window_5_greeting",
    )
