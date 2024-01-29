import math

# Ввод данных
width = float(input())
height = float(input())
paint_coverage = float(input())
can_volume = int(input())
reserve_percentage = int(input())

# Вычисление площади окрашивания
paint_area = width * height

# Вычисление необходимого количества литров краски с учетом запаса
required_liters = paint_area / paint_coverage * (1 + reserve_percentage / 100)

# Округление необходимого количества литров краски
required_liters = round(required_liters, 2)

# Вычисление количества банок краски (округление вверх)
cans_needed = math.ceil(required_liters / can_volume)

# Округление неиспользуемых литров краски
unused_liters = round(cans_needed * can_volume - required_liters, 2)

print(paint_area)
print(required_liters)
print(cans_needed)
print(unused_liters)
