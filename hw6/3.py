"""
Напишите программу принимающую ввод информации о треке(место в чарте, исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место, испонитель): название трека}
"""

track = {}
while True:
    place = input('Место: ')
    if place == 'off':
        break
    artist = input('Исполнитель: ')
    title = input('Название трека: ')
    track[(place, artist)] = title
print(track)