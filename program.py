print("Здравствуйте")

WATER_PER_KG = 30

user_name=input("Как вас зовут?")
user_name=user_name.title()
print(f"Ваше имя:{user_name}")

user_age=input("Сколько вам лет?")
user_age=int(user_age)

user_weight=input("Какой у вас вес?")
user_weight=int(user_weight)
weight=float(user_weight)

user_height=input("Какой у вас рост?")
user_height=int(user_height)
height_cm=float(user_height)
height_1 = height_cm / 100.0

bmi = weight / (height_1 ** 2)
round(bmi, 1)
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / 1000

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print(" "*50)
print("Расчет окончен. Будьте здоровы!")