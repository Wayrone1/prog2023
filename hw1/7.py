# Ввод стоимости одной единицы товара
cost_per_unit = int(input())

budget = 1572

# Вычисление количества единиц товара, которые можно купить
quantity = budget // cost_per_unit


print(quantity)
