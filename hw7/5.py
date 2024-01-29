"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""


def f():
    students = int(input('Введите кол-во учеников: '))
    all_languages = set()
    any_languages = set()
    for _ in range(students):
       num_languages = int(input('Введите кол-во языков, которые знает ученик: '))
       students_languages = set()
       for _ in range(num_languages):
           languages = input('Введите язык, который знает ученик: ')
           students_languages.add(languages)
       if not all_languages:
           all_languages = students_languages.copy()
       else:
           # Обновления множества языков, которые знают все ученики
           all_languages = all_languages.intersection(students_languages)
        # Обновление множества языков, которые знает хотя бы один ученик
       any_languages = any_languages.union(students_languages)
    print(len(all_languages), '-', list(all_languages))
    print(len(any_languages), '-', list(any_languages))
f()