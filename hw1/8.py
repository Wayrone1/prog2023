number = int(input())

# Извлечение цифр числ
digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10

sum_of_digits = digit1 + digit2 + digit3

print(sum_of_digits)
