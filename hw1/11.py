mass = float(input())
height_cm = float(input())

# Преобразование роста в метры
height_m = height_cm / 100

# Вычисление ИМТ
bmi = mass / (height_m ** 2)

# Округление ИМТ до 2 знаков после запятой
bmi = round(bmi, 2)

print(bmi)