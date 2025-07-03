hello-user = Hello { $username }. Choose an action.

button-button = Find dimensional tolerance.

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

### Handle errors

messages-tolerance_unavailable = ❌ Tolerance doesn't exists.
messages-dimension_unavailable = ❌ Tolerance dimension unavailable to size {$target_value}.
messages-deviation_unavailable = ❌ Tolerance deviation doesn't exists.
messages-wrong_value = Wrong value, please try again.
messages-wrong_tolerance_format = ⚠️ Wrong tolerance format {$name}.

errors-not_found = ❌ Not found: { $name }
errors-conflict = ⚠️ Conflict: { $name }
errors-unauthorized = 🔒 Unauthorized: { $name }
errors-forbidden = 🚫 Forbidden: { $name }
errors-bad_request = ⚠️ Bad request: { $name }
errors-unavailable_service = ⚠️ Unavailable service: { $name }
errors-validation_error = ⚠️ Validation error: { $name }
errors-unexpected_error = 🚨 Unexpected error, try again.
