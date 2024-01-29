"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def calculate(*numbers):
    if not numbers:
        return None
    average = sum(numbers) / len(numbers)
    above_average = [num for num in numbers if num > average]
    return average, above_average
result = calculate(1, 2, 3, 4, 5)
print(f'Среднее значение и числа, превышающие среднее: {result}')