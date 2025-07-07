hello-user = Hello { $username }. Choose an action.

button-button = Find dimensional tolerance.
button-transition_map = Find mapping for OSST tolerance.
button-transition_calc = Calculate cutting conditions.

button-pressed = You pressed the button.

no-copy = This type of update is not supported by the send_copy method.

text-method1 = Enter the tolerance value e.g 20H7.

tolerance-answer =
    upper deviation = {$upper}
    lower deviation = {$lower}
    max size = {$max}
    <b>avg size = {$avg}</b>
    min size = {$min}

next-step = You can do next:

ContinueAction-step = Continue

back-step = Return

### Steps

step-calc-first-message = Choose operation type:
step-calc-first-milling-button = Milling
step-calc-first-drilling-button = Drilling
step-calc-first-turning-button = Turning

### Map tolerance texts

map-tolerance-invite_text = Enter a russian OSST tolerance name.
map-tolerance-found_text = Next tolerances found: {$list}.

### Handle errors

messages-tolerance_unavailable = ❌ Tolerance doesn't exists.
messages-dimension_unavailable = ❌ Tolerance dimension unavailable to size {$target_value}.
messages-deviation_unavailable = ❌ Tolerance deviation doesn't exists.
messages-wrong_value = Wrong value, please try again.
messages-wrong_tolerance_format = ⚠️ Wrong tolerance format {$name}.

messages-old_tolerance_unavailable = ❌OSST tolerance doesn't exists.
messages-old_tolerance_relations_unavailable = ❌OSST tolerance relations doesn't exists.

messages-conditions-value_not_float = The value isn't a number.
messages-conditions-value_not_int = The value can't be a float number.
messages-conditions-wrong_value = The value must be greater than 0.

errors-not_found = ❌ Not found: { $name }
errors-conflict = ⚠️ Conflict: { $name }
errors-unauthorized = 🔒 Unauthorized: { $name }
errors-forbidden = 🚫 Forbidden: { $name }
errors-bad_request = ⚠️ Bad request: { $name }
errors-unavailable_service = ⚠️ Unavailable service: { $name }
errors-validation_error = ⚠️ Validation error: { $name }
errors-unexpected_error = 🚨 Unexpected error, try again.

### Conditions dialogs.

conditions-prompt-tool_diameter-text = Input a tool diameter:
conditions-prompt-part_diameter-text = Input a part diameter:
conditions-prompt-cutting_speed-text = Input cutting speed:
conditions-prompt-spindle_speed-text = Input spindle speed:
conditions-prompt-number_of_teeth-text = Input number of teeth:
conditions-prompt-feed_per_tooth-text = Input feed per tooth:
conditions-prompt-feed_rate-text = Input feed rate:

conditions-milling-tool_diameter-text = Tool diameter: {$value} mm.
conditions-milling-cutting_speed-text = Cutting speed: {$value} m/min.
conditions-milling-spindle_speed-text = Spindle speed: {$value} rev/min.
conditions-milling-number_of_teeth-text = Number of teeth: {$value} pieces.
conditions-milling-feed_per_tooth-text = Feed per tooth: {$value} mm.
conditions-milling-feed_rate-text = Feed rate: {$value} mm/min.
conditions-common-feed_per_rev-text = Feed per rev: {$value} mm/rev.
conditions-common-part_diameter-text = Part diameter: {$value} mm.


### Common

transition-button-forward = Forward ▶️
transition-button-back = ◀️ Back
transition-button-cancel = Quit
transition-button-return_prev = Return