"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
dict['1'], dict['5'] = dict['5'], dict['1']
del dict['2']
dict['new_key'] = 'new_value'
print(dict)