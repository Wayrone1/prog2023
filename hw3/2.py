sum = int(input('введите сумму к оплате'))
time = input('введите текущий час')
if time == '10' or time == '11' or time == '12':
    print(sum * 0.5)
elif time == '20' or time == '21' or time == '22':
    print(sum * 0.25)
else:
    print(sum)
