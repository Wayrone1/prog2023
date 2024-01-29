dis = input()
while dis.lower() != 'off':
    dis = input('Введите game: ')
    print(dis)
    if dis.lower() == 'game':
        print('Угадай число')
        for i in range(3):
            dis = int(input())
            if dis == 5:
                print('Вы выйграли билет')
            else:
                print('Повезет в следующий раз')
    else:
        print('Напишите off для выхода')
        dis = input()