"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""

import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python program.py <Цвета> <количество цветов>")
        return
    
    colors = sys.argv[1]
    num_colors = int(sys.argv[2])

    if len(sys.argv) != num_colors * 2 + 3:
        print("Error: Неверное количество цветов и HEX значений.")
        return

    print(f"Цвета: {colors}, количество цветов: {num_colors}")
    for i in range(3, len(sys.argv), 2):
        color_name = sys.argv[i]
        hex_value = sys.argv[i + 1]
        print(f"Цвет: {color_name}, HEX: {hex_value}")

if __name__ == "__main__":
    main()
