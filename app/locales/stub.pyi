from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    button: Button
    no: No
    text: Text
    tolerance: Tolerance
    next: Next
    ContinueAction: ContinueAction
    back: Back
    step: Step
    map: Map
    messages: Messages
    errors: Errors
    conditions: Conditions
    transition: Transition


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Hello { $username }. Choose an action."""]: ...


class Button:
    @staticmethod
    def button() -> Literal["""Find dimensional tolerance."""]: ...

    @staticmethod
    def transition_map() -> Literal["""Find mapping for OSST tolerance."""]: ...

    @staticmethod
    def transition_calc() -> Literal["""Calculate cutting conditions."""]: ...

    @staticmethod
    def pressed() -> Literal["""You pressed the button."""]: ...


class No:
    @staticmethod
    def copy() -> Literal["""This type of update is not supported by the send_copy method."""]: ...


class Text:
    @staticmethod
    def method1() -> Literal["""Enter the tolerance value e.g 20H7."""]: ...


class Tolerance:
    @staticmethod
    def answer(*, upper, lower, max, avg, min) -> Literal["""upper deviation = { $upper }
lower deviation = { $lower }
max size = { $max }
&lt;b&gt;avg size = { $avg }&lt;/b&gt;
min size = { $min }"""]: ...


class Next:
    @staticmethod
    def step() -> Literal["""You can do next:"""]: ...


class ContinueAction:
    @staticmethod
    def step() -> Literal["""Continue"""]: ...


class Back:
    @staticmethod
    def step() -> Literal["""Return"""]: ...


class Step:
    calc: StepCalc


class StepCalc:
    first: StepCalcFirst


class StepCalcFirst:
    milling: StepCalcFirstMilling
    drilling: StepCalcFirstDrilling
    turning: StepCalcFirstTurning

    @staticmethod
    def message() -> Literal["""Choose operation type:"""]: ...


class StepCalcFirstMilling:
    @staticmethod
    def button() -> Literal["""Milling"""]: ...


class StepCalcFirstDrilling:
    @staticmethod
    def button() -> Literal["""Drilling"""]: ...


class StepCalcFirstTurning:
    @staticmethod
    def button() -> Literal["""Turning"""]: ...


class Map:
    tolerance: MapTolerance


class MapTolerance:
    @staticmethod
    def invite_text() -> Literal["""Enter a russian OSST tolerance name."""]: ...

    @staticmethod
    def found_text(*, list) -> Literal["""Next tolerances found: { $list }."""]: ...


class Messages:
    conditions: MessagesConditions

    @staticmethod
    def tolerance_unavailable() -> Literal["""❌ Tolerance doesn&#39;t exists."""]: ...

    @staticmethod
    def dimension_unavailable(*, target_value) -> Literal["""❌ Tolerance dimension unavailable to size { $target_value }."""]: ...

    @staticmethod
    def deviation_unavailable() -> Literal["""❌ Tolerance deviation doesn&#39;t exists."""]: ...

    @staticmethod
    def wrong_value() -> Literal["""Wrong value, please try again."""]: ...

    @staticmethod
    def wrong_tolerance_format(*, name) -> Literal["""⚠️ Wrong tolerance format { $name }."""]: ...

    @staticmethod
    def old_tolerance_unavailable() -> Literal["""❌OSST tolerance doesn&#39;t exists."""]: ...

    @staticmethod
    def old_tolerance_relations_unavailable() -> Literal["""❌OSST tolerance relations doesn&#39;t exists."""]: ...


class MessagesConditions:
    @staticmethod
    def value_not_float() -> Literal["""The value isn&#39;t a number."""]: ...

    @staticmethod
    def value_not_int() -> Literal["""The value can&#39;t be a float number."""]: ...

    @staticmethod
    def wrong_value() -> Literal["""The value must be greater than 0."""]: ...


class Errors:
    @staticmethod
    def not_found(*, name) -> Literal["""❌ Not found: { $name }"""]: ...

    @staticmethod
    def conflict(*, name) -> Literal["""⚠️ Conflict: { $name }"""]: ...

    @staticmethod
    def unauthorized(*, name) -> Literal["""🔒 Unauthorized: { $name }"""]: ...

    @staticmethod
    def forbidden(*, name) -> Literal["""🚫 Forbidden: { $name }"""]: ...

    @staticmethod
    def bad_request(*, name) -> Literal["""⚠️ Bad request: { $name }"""]: ...

    @staticmethod
    def unavailable_service(*, name) -> Literal["""⚠️ Unavailable service: { $name }"""]: ...

    @staticmethod
    def validation_error(*, name) -> Literal["""⚠️ Validation error: { $name }"""]: ...

    @staticmethod
    def unexpected_error() -> Literal["""🚨 Unexpected error, try again."""]: ...


class Conditions:
    prompt: ConditionsPrompt
    milling: ConditionsMilling
    common: ConditionsCommon


class ConditionsPrompt:
    tool_diameter: ConditionsPromptTool_diameter
    cutting_speed: ConditionsPromptCutting_speed
    spindle_speed: ConditionsPromptSpindle_speed
    number_of_teeth: ConditionsPromptNumber_of_teeth
    feed_per_tooth: ConditionsPromptFeed_per_tooth
    feed_rate: ConditionsPromptFeed_rate


class ConditionsPromptTool_diameter:
    @staticmethod
    def text() -> Literal["""Input a tool diameter:"""]: ...


class ConditionsPromptCutting_speed:
    @staticmethod
    def text() -> Literal["""Input cutting speed:"""]: ...


class ConditionsPromptSpindle_speed:
    @staticmethod
    def text() -> Literal["""Input spindle speed:"""]: ...


class ConditionsPromptNumber_of_teeth:
    @staticmethod
    def text() -> Literal["""Input number of teeth:"""]: ...


class ConditionsPromptFeed_per_tooth:
    @staticmethod
    def text() -> Literal["""Input feed per tooth:"""]: ...


class ConditionsPromptFeed_rate:
    @staticmethod
    def text() -> Literal["""Input feed rate:"""]: ...


class ConditionsMilling:
    tool_diameter: ConditionsMillingTool_diameter
    cutting_speed: ConditionsMillingCutting_speed
    spindle_speed: ConditionsMillingSpindle_speed
    number_of_teeth: ConditionsMillingNumber_of_teeth
    feed_per_tooth: ConditionsMillingFeed_per_tooth
    feed_rate: ConditionsMillingFeed_rate


class ConditionsMillingTool_diameter:
    @staticmethod
    def text(*, value) -> Literal["""Tool diameter: { $value } mm."""]: ...


class ConditionsMillingCutting_speed:
    @staticmethod
    def text(*, value) -> Literal["""Cutting speed: { $value } m/min."""]: ...


class ConditionsMillingSpindle_speed:
    @staticmethod
    def text(*, value) -> Literal["""Spindle speed: { $value } rev/min."""]: ...


class ConditionsMillingNumber_of_teeth:
    @staticmethod
    def text(*, value) -> Literal["""Number of teeth: { $value } pieces."""]: ...


class ConditionsMillingFeed_per_tooth:
    @staticmethod
    def text(*, value) -> Literal["""Feed per tooth: { $value } mm."""]: ...


class ConditionsMillingFeed_rate:
    @staticmethod
    def text(*, value) -> Literal["""Feed rate: { $value } mm/min."""]: ...


class ConditionsCommon:
    feed_per_rev: ConditionsCommonFeed_per_rev
    part_diameter: ConditionsCommonPart_diameter


class ConditionsCommonFeed_per_rev:
    @staticmethod
    def text(*, value) -> Literal["""Feed per rev: { $value } mm/rev."""]: ...


class ConditionsCommonPart_diameter:
    @staticmethod
    def text(*, value) -> Literal["""Part diameter: { $value } mm."""]: ...


class Transition:
    button: TransitionButton


class TransitionButton:
    @staticmethod
    def forward() -> Literal["""Forward ▶️"""]: ...

    @staticmethod
    def back() -> Literal["""◀️ Back"""]: ...

    @staticmethod
    def cancel() -> Literal["""Quit"""]: ...

    @staticmethod
    def return_prev() -> Literal["""Return"""]: ...

