### Start dialog
dialog-start-prompt-text = Hello { $username }. Choose an action.
dialog-start-button-tolerance = Find dimensional tolerance.
dialog-start-button-old_tolerance = Find mapping for OSST tolerance.
dialog-start-button-conditions = Calculate cutting conditions.

### Tolerance dialog
tolerance-prompt-text = Enter the tolerance value e.g 20H7.
tolerance-prompt-next-text = You can do next:
tolerance-answer =
    upper deviation = {$upper}
    lower deviation = {$lower}
    max size = {$max}
    <b>avg size = {$avg}</b>
    min size = {$min}

### Old tolerance texts

old-tolerance-invite_text = Enter a russian OSST tolerance name.
old-tolerance-found_text = Next tolerances found: {$list}.

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

### Conditions dialogs.

conditions-start-prompt = Choose operation type:
conditions-start-button-milling = Milling
conditions-start-button-drilling = Drilling
conditions-start-button-turning = Turning

conditions-prompt-tool_diameter-text = Input a tool diameter:
conditions-prompt-part_diameter-text = Input a part diameter:
conditions-prompt-cutting_speed-text = Input cutting speed:
conditions-prompt-spindle_speed-text = Input spindle speed:
conditions-prompt-number_of_teeth-text = Input number of teeth:
conditions-prompt-feed_per_tooth-text = Input feed per tooth:
conditions-prompt-feed_per_rev-text = Input feed per rev:
conditions-prompt-feed_rate-text = Input feed rate:

conditions-common-tool_diameter-text = Tool diameter: {$value} mm.
conditions-common-cutting_speed-text = Cutting speed: {$value} m/min.
conditions-common-spindle_speed-text = Spindle speed: {$value} rev/min.
conditions-common-number_of_teeth-text = Number of teeth: {$value} pieces.
conditions-common-feed_per_tooth-text = Feed per tooth: {$value} mm.
conditions-common-feed_rate-text = Feed rate: {$value} mm/min.
conditions-common-feed_per_rev-text = Feed per rev: {$value} mm/rev.
conditions-common-part_diameter-text = Part diameter: {$value} mm.


### Common transitions

transition-button-forward = Forward ▶️
transition-button-back = ◀️ Back
transition-button-cancel = Quit
transition-button-return_prev = Return
transition-button-continue_dialog = Continue