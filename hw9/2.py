"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""


def taxi(km):
    rate = 4.00
    fare_140m = 0.25
    meters = km * 1000
    blocks = meters / 140
    summ = rate + (blocks * fare_140m)
    return summ
distance = float(input('Введите расстояние поездки в километрах: '))
result = taxi(distance)
print(f'Сумма для оплаты такси: ${result:.2f}')