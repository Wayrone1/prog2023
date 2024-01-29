username = input('ФИО полностью')
surname_name_patronymic = username.split()

surname = surname_name_patronymic[0]
name = surname_name_patronymic[1][0] + '.'
patronymic = surname_name_patronymic[2][0] + '.'
print(surname, name + patronymic)