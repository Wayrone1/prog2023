cost = int(input())
while cost != 0:
    skidka = int(input())
    cost -= skidka
    if cost < 0:
        cost = 0