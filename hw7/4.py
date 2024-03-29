"""
Вася давно мечтает выиграть олимпиаду по информатике.
У него всего три слабых места: циклы, массивы и строки.
Перед сегодняшним турниром Вася провёл интенсивную подготовку, в ходе которой он решил A задач на циклы,
B задач на массивы и C задач на строки.
Впоследствии выяснилось, что из решённых задач D были и на циклы, и на массивы, E – на циклы и на строки,
F – на строки и на массивы. И даже было G задач, которые включали и циклы, и строки, и массивы.
Помогите Васе вычислить, сколько всего различных задач он решил.
Введите результат для всех 3 входных данных
"""
first = "0 0 0 0 0 0 0" #Вывод должен быть 0
second = "1 1 1 0 0 0 0" # Вывод должен быть 3
third = "1 1 1 1 1 1 1" # Вывод должен быть 1
def calculate_solved_tasks(data):
    A, B, C, D, E, F, G = map(int, data.split())
    total_solved = A + B + C - D - E - F + G
    return max(total_solved, 0)

first_result = calculate_solved_tasks(first)
second_result = calculate_solved_tasks(second)
third_result = calculate_solved_tasks(third)

print(first_result)
print(second_result)
print(third_result)
