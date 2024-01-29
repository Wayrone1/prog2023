"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""



def calculate(weight, height):
    return weight / (height * height)
78
def process(index):
    if index < 18.5:
        print("Недостаточный вес")
    elif 18.5 <= index < 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

def f():
    weight = float(input("Введите вес (в килограммах): "))
    height = float(input("Введите рост (в метрах): "))
    bmi_index = calculate(weight, height)
    print("Индекс массы тела:", bmi_index)
    process(bmi_index)
f()