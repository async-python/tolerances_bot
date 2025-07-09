"""Conditions controller."""

from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from app.schemas import ConditionSchema
from app.utils.calculators import (
    calculate_spindle_speed,
    calculate_cutting_speed,
    calculate_feed_rate,
    calculate_feed_per_tooth,
)
from core.exceptions.error_classes.conditions import ConditionsException

if TYPE_CHECKING:
    from app.locales.stub import TranslatorRunner


class ValueType(Enum):
    """Conditions value types."""

    DIAMETER = "DIAMETER"
    CUTTING_SPEED = "CUTTING_SPEED"
    SPINDLE_SPEED = "SPINDLE_SPEED"
    NUMBER_OF_TEETH = "NUMBER_OF_TEETH"
    FEED_PER_TOOTH = "FEED_PER_TOOTH"
    FEED_RATE = "FEED_RATE"


class ConditionsController:
    """Conditions controller class."""

    FIELD_MAP = {
        ValueType.DIAMETER: "tool_diameter",
        ValueType.CUTTING_SPEED: "cutting_speed",
        ValueType.SPINDLE_SPEED: "spindle_speed",
        ValueType.NUMBER_OF_TEETH: "number_of_teeth",
        ValueType.FEED_PER_TOOTH: "feed_per_tooth",
        ValueType.FEED_RATE: "feed_rate",
    }

    @classmethod
    async def process_conditions(
        cls,
        new_value: str,
        kind_of_value: ValueType,
        conditions: dict,
        i18n: "TranslatorRunner",
    ) -> ConditionSchema:
        """Calculate and recalculate milling conditions."""
        conditions_model = ConditionSchema(**conditions)

        # set new value
        field_name = cls.FIELD_MAP[kind_of_value]
        if kind_of_value != ValueType.NUMBER_OF_TEETH:
            await ConditionsException.raise_exception_if_not_float(
                value=new_value,
                i18n=i18n,
            )
        else:
            await ConditionsException.raise_exception_if_not_int(
                value=new_value,
                i18n=i18n,
            )
        await ConditionsException.raise_exception_if_zero_or_less(
            value=new_value,
            i18n=i18n,
        )
        value = (
            Decimal(new_value.replace(",", "."))
            if kind_of_value != ValueType.NUMBER_OF_TEETH
            else int(new_value)
        )
        setattr(conditions_model, field_name, value)

        # calculate spindle_speed if CUTTING_SPEED or DIAMETER changed
        await cls._process_spindle_speed(
            kind_of_value=kind_of_value,
            conditions_model=conditions_model,
        )

        # calculate cutting_speed if SPINDLE_SPEED changed
        await cls._process_cutting_speed(
            kind_of_value=kind_of_value,
            conditions_model=conditions_model,
        )

        # calculate feed_rate if it does not direct changed
        await cls._process_feed_rate(
            kind_of_value=kind_of_value,
            conditions_model=conditions_model,
        )

        # calculate feed_per_tooth if feed_rate changed
        await cls._process_feed_per_tooth(
            kind_of_value=kind_of_value,
            conditions_model=conditions_model,
        )
        return conditions_model

    @classmethod
    async def _process_spindle_speed(
        cls,
        kind_of_value: ValueType,
        conditions_model: ConditionSchema,
    ) -> None:
        """Calculate spindle_speed if CUTTING_SPEED or DIAMETER changed."""
        if kind_of_value in {ValueType.CUTTING_SPEED, ValueType.DIAMETER}:
            if (
                conditions_model.tool_diameter
                and conditions_model.cutting_speed
            ):
                conditions_model.spindle_speed = await calculate_spindle_speed(
                    cutting_speed=conditions_model.cutting_speed,
                    tool_diameter=conditions_model.tool_diameter,
                )
        return

    @classmethod
    async def _process_cutting_speed(
        cls,
        kind_of_value: ValueType,
        conditions_model: ConditionSchema,
    ) -> None:
        """Calculate cutting_speed if SPINDLE_SPEED changed."""
        if kind_of_value == ValueType.SPINDLE_SPEED:
            if (
                conditions_model.tool_diameter
                and conditions_model.spindle_speed
            ):
                conditions_model.cutting_speed = await calculate_cutting_speed(
                    spindle_speed=conditions_model.spindle_speed,
                    tool_diameter=conditions_model.tool_diameter,
                )
        return

    @classmethod
    async def _process_feed_rate(
        cls,
        kind_of_value: ValueType,
        conditions_model: ConditionSchema,
    ) -> None:
        """Calculate feed_rate if it does not direct changed."""
        if kind_of_value != ValueType.FEED_RATE:
            if (
                conditions_model.spindle_speed
                and conditions_model.number_of_teeth
                and conditions_model.feed_per_tooth
            ):
                conditions_model.feed_rate = await calculate_feed_rate(
                    spindle_speed=conditions_model.spindle_speed,
                    feed_per_tooth=conditions_model.feed_per_tooth,
                    number_of_teeth=conditions_model.number_of_teeth,
                )
        return

    @classmethod
    async def _process_feed_per_tooth(
        cls,
        kind_of_value: ValueType,
        conditions_model: ConditionSchema,
    ) -> None:
        """Calculate feed_per_tooth if feed_rate changed."""
        if kind_of_value == ValueType.FEED_RATE:
            if (
                conditions_model.spindle_speed
                and conditions_model.number_of_teeth
                and conditions_model.feed_rate
            ):
                conditions_model.feed_per_tooth = (
                    await calculate_feed_per_tooth(
                        feed_rate=conditions_model.feed_rate,
                        spindle_speed=conditions_model.spindle_speed,
                        number_of_teeth=conditions_model.number_of_teeth,
                    )
                )
        return
