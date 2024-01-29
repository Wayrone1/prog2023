"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def print_non_none_values(param1=None, param2=None, param3=None):
    if param1 is not None:
        print("Параметр 1:", param1)
    if param2 is not None:
        print("Параметр 2:", param2)
    if param3 is not None:
        print("Параметр 3:", param3)

# Пример использования функции
print_non_none_values(param1="Значение1", param2=None, param3="Значение3")
