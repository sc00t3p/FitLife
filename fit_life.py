# Проект FitLife - MVP версия 1.0

print('Вас приветствует помощник сервиса FitLife')
user_name = input('Укажите ваше имя: ')
print(f'Здравсвуйте, {user_name}!')
user_age = int(input('Укажите ваш возраст: '))


def get_age_string(age):
    """Разделяет возраст на годы, года и лет для корректного отображения."""
    last_digit = age % 10
    last_two_digits = age % 100

    if 11 <= last_two_digits <= 14:
        return f"{user_age} лет"

    if last_digit == 1:
        return f"{user_age} год"
    if 2 <= last_digit <= 4:
        return f"{user_age} года"
    return f"{user_age} лет"


print(f'{user_name}, вам {get_age_string(user_age)}. Отлично!')

user_weight = float(input('Укажите ваш вес в килограммах: '))
user_height = float(input('Укажите ваш рост в метрах (например, 1.75): '))
bmi = user_weight / (user_height ** 2)  # расчет индекса массы тела (BMI)
round(bmi, 1)
water_ml = user_weight * 30  # расчет кол-ва воды (30 мл на кг веса)
water_l = water_ml / 1000   # расчет рекомендуемого количества воды в литрах

print(f'Отчет для пользователя : {user_name} ({get_age_string(user_age)})')
print(f'Ваш индекс массы тела (BMI) составляет: {bmi:.1f}')
print(f'Рекомендуемое количество воды в день: {water_l:.2f} литров')

print('Расчет окончен. Будьте здоровы!')
