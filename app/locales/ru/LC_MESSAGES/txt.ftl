hello-user = Привет, { $username }. Выберите действие.

button-button = Найти допуск размера
button-transition_map = Найти аналог ОССТ допуска.
button-transition_calc = Калькулятор режимов обработки.

button-pressed = Вы нажали на кнопку

no-copy = Данный тип апдейтов не поддерживается методом send_copy

text-method1 = Введите значение допуска в формате 20H7

tolerance-answer =
    верхнее отклонение = {$upper}
    нижнее отклонение = {$lower}
    макс. размер = {$max}
    <b>средний размер = {$avg}</b>
    мин. размер = {$min}

next-step = Дальше вы можете:

ContinueAction-step = Продолжить

back-step = Вернуться

### Steps

step-calc-first-message = Выберите тип операции:
step-calc-first-milling-button = Фрезерование
step-calc-first-drilling-button = Сверление
step-calc-first-turning-button = Точение

### Map tolerance texts

map-tolerance-invite_text = Введите наименование допуска в система ОССТ.
map-tolerance-found_text = Найдены следующие соответствия допусков: {$list}.

### Обработка ошибок

messages-tolerance_unavailable = ❌ Допуск не существует.
messages-dimension_unavailable = ❌ Для данного размера допуск не существует {$target_value}.
messages-deviation_unavailable = ❌ Для данного допуска не существует такого размера.
messages-wrong_value = Некорректный ввод, попробуйте еще раз.
messages-wrong_tolerance_format = ⚠️ Неправильный формат допуска {$name}.

messages-old_tolerance_unavailable = ❌ ОССТ допуск не существует.
messages-old_tolerance_relations_unavailable = ❌Для ОССТ допуска не существует аналогов.

messages-conditions-value_not_float = Значение должно быть числом.
messages-conditions-value_not_int = Значение должно быть целым числом.
messages-conditions-wrong_value = Значение должно быть больше 0.

errors-not_found = ❌ Не найдено: { $name }
errors-conflict = ⚠️ Конфликт: { $name }
errors-unauthorized = 🔒 Нет доступа: { $name }
errors-forbidden = 🚫 Запрещено: { $name }
errors-bad_request = ⚠️ Неверный запрос: { $name }
errors-unavailable_service = ⚠️ Сервис недоступен: { $name }
errors-validation_error = ⚠️ Ошибка валидации: { $name }
errors-unexpected_error = 🚨 Произошла непредвиденная ошибка, пожалуйста, попробуйте снова.

### Conditions dialogs.

conditions-prompt-tool_diameter-text = Введите диаметр инструмента:
conditions-prompt-part_diameter-text = Введите диаметр заготовки:
conditions-prompt-cutting_speed-text = Введите скорость резания:
conditions-prompt-spindle_speed-text = Введите обороты шпинделя:
conditions-prompt-number_of_teeth-text = Введите количество зубьев:
conditions-prompt-feed_per_tooth-text = Введите подачу на зуб:
conditions-prompt-feed_per_rev-text = Введите подачу на оборот:
conditions-prompt-feed_rate-text = Введите минутную подачу:

conditions-milling-tool_diameter-text = Диаметр фрезы: {$value} mm.
conditions-milling-cutting_speed-text = Скорость резания: {$value} m/min.
conditions-milling-spindle_speed-text = Обороты шпинделя: {$value} rev/min.
conditions-milling-number_of_teeth-text = Число зубьев: {$value} pieces.
conditions-milling-feed_per_tooth-text = Подача на зуб: {$value} mm.
conditions-milling-feed_rate-text = Минутная подача: {$value} mm/min.
conditions-common-feed_per_rev-text = Подача на оборот: {$value} mm/rev.
conditions-common-part_diameter-text = Диаметр заготовки: {$value} mm.

### Common

transition-button-forward = Вперед ▶️
transition-button-back = ◀️ Назад
transition-button-cancel = Выйти
transition-button-return_prev = Вернуться