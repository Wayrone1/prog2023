Games = []
while True:
    game = input('Введите название игры')
    if game == '0':
        break
    elif game in Games:
        print ('Эта игра уже записана')
    else:
        Games.append(game)
    Games.sort()

    print ('Список игр', Games)