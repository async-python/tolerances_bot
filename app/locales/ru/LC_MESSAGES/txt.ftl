### Start dialog
dialog-start-prompt-text = Привет, { $username }. Выберите действие.
dialog-start-button-tolerance = Найти допуск размера
dialog-start-button-old_tolerance = Найти аналог ОССТ допуска.
dialog-start-button-conditions = Калькулятор режимов обработки.

### Tolerance dialog
tolerance-prompt-text = Введите значение допуска в формате 20H7
tolerance-prompt-next-text = Дальше вы можете:
tolerance-answer =
    верхнее отклонение = {$upper}
    нижнее отклонение = {$lower}
    макс. размер = {$max}
    <b>средний размер = {$avg}</b>
    мин. размер = {$min}

### Old tolerance texts

old-tolerance-invite_text = Введите наименование допуска в система ОССТ.
old-tolerance-found_text = Найдены следующие соответствия допусков: {$list}.

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

### Conditions dialogs.

conditions-start-prompt = Выберите тип операции:
conditions-start-button-milling = Фрезерование
conditions-start-button-drilling = Сверление
conditions-start-button-turning = Точение

conditions-prompt-tool_diameter-text = Введите диаметр инструмента:
conditions-prompt-part_diameter-text = Введите диаметр заготовки:
conditions-prompt-cutting_speed-text = Введите скорость резания:
conditions-prompt-spindle_speed-text = Введите обороты шпинделя:
conditions-prompt-number_of_teeth-text = Введите количество зубьев:
conditions-prompt-feed_per_tooth-text = Введите подачу на зуб:
conditions-prompt-feed_per_rev-text = Введите подачу на оборот:
conditions-prompt-feed_rate-text = Введите минутную подачу:

conditions-common-tool_diameter-text = Диаметр фрезы: {$value} mm.
conditions-common-cutting_speed-text = Скорость резания: {$value} m/min.
conditions-common-spindle_speed-text = Обороты шпинделя: {$value} rev/min.
conditions-common-number_of_teeth-text = Число зубьев: {$value} pieces.
conditions-common-feed_per_tooth-text = Подача на зуб: {$value} mm.
conditions-common-feed_rate-text = Минутная подача: {$value} mm/min.
conditions-common-feed_per_rev-text = Подача на оборот: {$value} mm/rev.
conditions-common-part_diameter-text = Диаметр заготовки: {$value} mm.

### Common transitions

transition-button-forward = Вперед ▶️
transition-button-back = ◀️ Назад
transition-button-cancel = Выйти
transition-button-return_prev = Вернуться
transition-button-continue_dialog = Продолжить