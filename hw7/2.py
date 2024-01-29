"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
printSet = set()

all_immutable = all(isinstance(item, (int, float, complex, str, tuple, frozenset)) for item in printSet)
print(all_immutable)

mutable_elements = [item for item in printSet if not isinstance(item, (int, float, complex, str, tuple, frozenset))]
print("Mutable elements:", mutable_elements)