"""Dialog getters."""

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from aiogram.types import User
from app.schemas import ConditionSchema
from collections.abc import Callable


async def get_data_window_generic(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    active_field: str,
    window_greeting_key: str,
    data_key: str,
    field_map: dict[str, callable],
    buttons: dict[str, str],
    window_greeting_getter: Callable[[TranslatorRunner], str] | None = None,
    **kwargs: dict,
) -> dict[str, str]:
    """Universal getter for milling, drilling, turning
    windows with flexible window prompt."""
    data = dialog_manager.dialog_data.get(data_key, {})
    conditions = ConditionSchema(**data)

    if window_greeting_getter:
        window_greeting = window_greeting_getter(i18n)
    else:
        window_greeting = getattr(i18n.conditions.prompt, active_field).text()

    result = {
        window_greeting_key: window_greeting,
        "button_forward": i18n.transition.button.forward(),
        "button_back": i18n.transition.button.back(),
        "button_cancel": i18n.transition.button.cancel(),
        "button_return": i18n.transition.button.return_prev(),
    }

    for field, formatter in field_map.items():
        val = getattr(conditions, field, None) or "__"
        prefix = "->" if field == active_field else "--"
        result[field] = f"{prefix}{formatter(i18n, val)}"

    result |= buttons
    return result
