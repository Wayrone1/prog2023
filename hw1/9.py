number = int(input())

# Извлечение цифр числа
digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10

# Переворот числа и формирование нового числа
reversed_number = digit3 * 100 + digit2 * 10 + digit1

print(reversed_number)
