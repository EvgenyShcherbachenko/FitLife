# Проект FitLife - MVP версия 1.0

# 1. Константы
WATER_ML_PER_KG = 30
ML_IN_LITER = 1000

# 2. Знакомство
print("Доброго времени суток! Давайте познакомимся.")
user_name = input("Введите свое имя: ").strip()
print("Очень приятно", user_name, sep=", ")
try:
    user_age = int(input("Укажите свой возраст: "))
except ValueError:
    raise ValueError("Ошибка: возраст нужно указать целым числом. Пример: 36")

# 3. Сбор данных
try:
    user_weight = float(input("Укажите свой вес в кг: "))
except ValueError:
    raise ValueError("Ошибка: вес нужно указать числом.")
try:
    user_height = float(input("Укажите свой рост в метрах (пример: 1.77): "))
except ValueError:
    raise ValueError("Ошибка: рост нужно указать числом и использовать точку.")
print("Отлично! Теперь рассчитаем")

# 4. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / ML_IN_LITER

# 5. Вывод результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.2f} л. в день")
print("Расчет окончен. Будьте здоровы!")
