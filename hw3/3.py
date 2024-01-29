price1 = int(input('цена первого товара'))
price2 = int(input('цена второго товара'))
price3 = int(input('цена третьего товара'))

if price1 < price2 < price3:
    sum = (price1 + price2 + price3) / 2
    print('Акция!', sum)
elif price1 > price2 > price3:
    sum = (price1 + price2 + price3) / 3
    print('Акция!', sum)
else:
    print(price1 + price2 + price3)