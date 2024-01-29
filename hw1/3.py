def negative_color(brightness):
    # Проверка, что значение находится в диапазоне от 0 до 255
    if 0 <= brightness <= 255:
        # Вычисление цвета негатива
        negative_brightness = 255 - brightness
        return negative_brightness
    else:
        # Вывод ошибки, если значение вне диапазона
        return "Ошибка: Значение должно быть от 0 до 255"

# Ввод значения яркости пикселя
brightness = int(input())


result = negative_color(brightness)
print(result)