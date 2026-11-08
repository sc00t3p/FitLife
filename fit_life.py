# Проект FitLife - MVP версия 1.0

print('Вас приветствует помощник сервиса FitLife')
user_name = input('Укажите ваше имя: ')
print(f'Здравствуйте, {user_name}!')
user_age = int(input('Укажите ваш возраст: '))


def get_age_string(age):
    """Разделяет возраст на годы, года и лет для корректного отображения."""
    last_digit = age % 10
    last_two_digits = age % 100

    if 11 <= last_two_digits <= 14:
        return f"{age} лет."

    if last_digit == 1:
        return f"{age} год."
    if 2 <= last_digit <= 4:
        return f"{age} года."
    return f"{age} лет."


name_report = get_age_string(user_age)
print('Вам,', name_report, 'Отлично!')

user_weight = float(input('Укажите ваш вес в килограммах: '))
user_height = float(input('Укажите ваш рост в метрах (например, 1.75): '))
bmi = user_weight / (user_height**2)  # расчет индекса массы тела (BMI)
water_ml = user_weight * 30  # расчет кол-ва воды (30 мл на кг веса)
water_l = water_ml / 1000   # расчет рекомендуемого количества воды в литрах

user_bmi = f'{bmi:.1f}'
water_norm_day = f'{water_l:.2f}'

print('Отчет для пользователя : ', user_name, name_report)
print('Ваш индекс массы тела (BMI) составляет:', user_bmi)
print('Рекомендуемое количество воды в день:', water_norm_day, 'литров')

print('Расчет окончен. Будьте здоровы!')
