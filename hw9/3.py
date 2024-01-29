"""
Напишите программу, которая будет складывать числа, введенные поль-
зователем. Сигналом к окончанию ввода должна служить пустая строка.
Отобразите на экране сумму значений (или 0.0, если пользователь сразу
же пропустил ввод). Решите эту задачу с использованием рекурсии. В ва-
шей программе не должны присутствовать циклы.
Подсказка. В теле вашей рекурсивной функции должен производиться запрос одно-
го числа у пользователя, после чего должно быть принято решение о том, произво-
дить ли еще один рекурсивный вызов. Ваша функция не должна принимать аргумен-
тов, а возвращать будет числовое значе
"""


def f():
    user = input('Введите число, а для завершения введите пустую строку: ')
    if user == '':
        return 0.0
    elif user.replace('.', '').isdigit():
        number = float(user)
        return number + f()
    else:
        print('Некорректный ввод. Введите число. ')
        return f()
result = f()
print(f'Сумма введенных чисел: {result}')