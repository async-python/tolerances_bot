"""Turning calculation getters."""

from typing import TYPE_CHECKING, Any

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
    val: i18n.conditions.common.part_diameter.text(value=val),
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


def turning_part_diameter_prompt(
    i18n: "TranslatorRunner",
) -> str:
    """Getter for part diameter prompt."""
    return i18n.conditions.prompt.part_diameter.text()


def turning_feed_per_rev_prompt(
    i18n: "TranslatorRunner",
) -> str:
    """Getter for per rev prompt."""
    return i18n.conditions.prompt.feed_per_rev.text()


async def get_data_turning_window_1(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter part diameter window 1."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="tool_diameter",
        window_greeting_key="window_1_greeting",
        data_key="turning",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
        window_greeting_getter=turning_part_diameter_prompt,
    )


async def get_data_turning_window_2(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter cutting speed window 2."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="cutting_speed",
        window_greeting_key="window_2_greeting",
        data_key="turning",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_turning_window_3(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter spindle speed window 3."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="spindle_speed",
        window_greeting_key="window_3_greeting",
        data_key="turning",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )


async def get_data_turning_window_4(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter feed per rev window 4."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_per_tooth",
        window_greeting_key="window_4_greeting",
        data_key="turning",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
        window_greeting_getter=turning_feed_per_rev_prompt,
    )


async def get_data_turning_window_5(
    *args: Any,
    **kwargs: dict,
) -> dict[str, str]:
    """Getter feed rate window 5."""
    return await get_data_window_generic(
        *args,
        **kwargs,
        active_field="feed_rate",
        window_greeting_key="window_5_greeting",
        data_key="turning",
        field_map=FIELD_MAP,
        buttons=BUTTONS,
    )
