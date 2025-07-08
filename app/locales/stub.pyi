from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    dialog: Dialog
    tolerance: Tolerance
    old: Old
    messages: Messages
    conditions: Conditions
    transition: Transition


class Dialog:
    start: DialogStart


class DialogStart:
    prompt: DialogStartPrompt
    button: DialogStartButton


class DialogStartPrompt:
    @staticmethod
    def text(*, username) -> Literal["""Hello { $username }. Choose an action."""]: ...


class DialogStartButton:
    @staticmethod
    def tolerance() -> Literal["""Find dimensional tolerance."""]: ...

    @staticmethod
    def old_tolerance() -> Literal["""Find mapping for OSST tolerance."""]: ...

    @staticmethod
    def conditions() -> Literal["""Calculate cutting conditions."""]: ...


class Tolerance:
    prompt: TolerancePrompt

    @staticmethod
    def answer(*, upper, lower, max, avg, min) -> Literal["""upper deviation = { $upper }
lower deviation = { $lower }
max size = { $max }
&lt;b&gt;avg size = { $avg }&lt;/b&gt;
min size = { $min }"""]: ...


class TolerancePrompt:
    next: TolerancePromptNext

    @staticmethod
    def text() -> Literal["""Enter the tolerance value e.g 20H7."""]: ...


class TolerancePromptNext:
    @staticmethod
    def text() -> Literal["""You can do next:"""]: ...


class Old:
    tolerance: OldTolerance


class OldTolerance:
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


class Conditions:
    start: ConditionsStart
    prompt: ConditionsPrompt
    common: ConditionsCommon


class ConditionsStart:
    button: ConditionsStartButton

    @staticmethod
    def prompt() -> Literal["""Choose operation type:"""]: ...


class ConditionsStartButton:
    @staticmethod
    def milling() -> Literal["""Milling"""]: ...

    @staticmethod
    def drilling() -> Literal["""Drilling"""]: ...

    @staticmethod
    def turning() -> Literal["""Turning"""]: ...


class ConditionsPrompt:
    tool_diameter: ConditionsPromptTool_diameter
    part_diameter: ConditionsPromptPart_diameter
    cutting_speed: ConditionsPromptCutting_speed
    spindle_speed: ConditionsPromptSpindle_speed
    number_of_teeth: ConditionsPromptNumber_of_teeth
    feed_per_tooth: ConditionsPromptFeed_per_tooth
    feed_per_rev: ConditionsPromptFeed_per_rev
    feed_rate: ConditionsPromptFeed_rate


class ConditionsPromptTool_diameter:
    @staticmethod
    def text() -> Literal["""Input a tool diameter:"""]: ...


class ConditionsPromptPart_diameter:
    @staticmethod
    def text() -> Literal["""Input a part diameter:"""]: ...


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


class ConditionsPromptFeed_per_rev:
    @staticmethod
    def text() -> Literal["""Input feed per rev:"""]: ...


class ConditionsPromptFeed_rate:
    @staticmethod
    def text() -> Literal["""Input feed rate:"""]: ...


class ConditionsCommon:
    tool_diameter: ConditionsCommonTool_diameter
    cutting_speed: ConditionsCommonCutting_speed
    spindle_speed: ConditionsCommonSpindle_speed
    number_of_teeth: ConditionsCommonNumber_of_teeth
    feed_per_tooth: ConditionsCommonFeed_per_tooth
    feed_rate: ConditionsCommonFeed_rate
    feed_per_rev: ConditionsCommonFeed_per_rev
    part_diameter: ConditionsCommonPart_diameter


class ConditionsCommonTool_diameter:
    @staticmethod
    def text(*, value) -> Literal["""Tool diameter: { $value } mm."""]: ...


class ConditionsCommonCutting_speed:
    @staticmethod
    def text(*, value) -> Literal["""Cutting speed: { $value } m/min."""]: ...


class ConditionsCommonSpindle_speed:
    @staticmethod
    def text(*, value) -> Literal["""Spindle speed: { $value } rev/min."""]: ...


class ConditionsCommonNumber_of_teeth:
    @staticmethod
    def text(*, value) -> Literal["""Number of teeth: { $value } pieces."""]: ...


class ConditionsCommonFeed_per_tooth:
    @staticmethod
    def text(*, value) -> Literal["""Feed per tooth: { $value } mm."""]: ...


class ConditionsCommonFeed_rate:
    @staticmethod
    def text(*, value) -> Literal["""Feed rate: { $value } mm/min."""]: ...


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

    @staticmethod
    def continue_dialog() -> Literal["""Continue"""]: ...

