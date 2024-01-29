from datetime import datetime, timedelta

# Ввод времени в секундах
timestamp = int(input())

# Начальная дата (Unix Epoch)
start_date = datetime(1970, 1, 1)

# Разница в секундах между начальной датой и заданным временем
time_difference = timedelta(seconds=timestamp)

# Вычисление конечной даты
end_date = start_date + time_difference

print(end_date.year)
