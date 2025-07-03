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
    messages: Messages
    errors: Errors


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Hello { $username }. Choose an action."""]: ...


class Button:
    @staticmethod
    def button() -> Literal["""Find dimensional tolerance."""]: ...

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


class Messages:
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

