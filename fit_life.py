print('Вас приветствует помощник сервиса FitLife')
while True:
    user_name = input('Укажите ваше имя: ').strip()
    if user_name:
        break
    print('Попробуйте еще раз.')
    print(f'Здравствуйте, {user_name}!')

def get_age_string(age):
    last_digit = age % 10
    last_two_digits = age % 100
    if 11 <= last_two_digits <= 14:
        return f"{age} лет."
    if last_digit == 1:
        return f"{age} год."
    if 2 <= last_digit <= 4:
        return f"{age} года."
    return f"{age} лет."


while True:
    user_age_input = input('Укажите ваш возраст: ').strip()
    if user_age_input.isdigit():
        user_age = int(user_age_input)
        if 18 <= user_age <= 99:
            break
        else:
            print('Введите возраст в диапазоне от 18 до 99')
    else:
        print('Введите корректный возраст цифрами')

print(f'{user_name}, вам {get_age_string(user_age)}. Отлично!')


while True:
    try:
        user_weight = float(input('Пожалуйста, укажите ваш вес в килограммах: '))
        if 25 <= user_weight <= 250:
            break
        print('Ошибка: вес должен быть в диапазоне от 25 до 250 кг.')
    except ValueError:
        print('Пожалуйста, введите число (например, 75.5)')

while True:
    try:
        user_height = float(input('Пожалуйста, укажите ваш рост в метрах (например, 1.75): '))
        if 0.5 <= user_height <= 2.5:
            break
        print('Ошибка: рост должен быть в диапазоне от 0.5 до 2.5 метров.')
    except ValueError:
        print('Пожалуйста, введите число через точку (например, 1.75)')


bmi = user_weight / (user_height**2)  
water_l = user_weight * 30 / 1000   
user_bmi = f'{bmi:.1f}'
water_norm_day = f'{water_l:.2f}'
print(f'Отчет для пользователя: {user_name} ({get_age_string(user_age)})')
print(f'Ваш индекс массы тела (BMI) составляет: {user_bmi}')
print(f'Рекомендуемое количество воды в день: {water_norm_day} литров')
print('Расчет окончен. Будьте здоровы!')
 