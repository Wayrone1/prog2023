# Ввод курса рубля к доллару и курса доллара к евро
rub_to_usd = float(input())
usd_to_eur = float(input())

# Вычисление курса евро к рублю
eur_to_rub = 1 / (rub_to_usd * usd_to_eur)


eur_to_rub = round(eur_to_rub, 2)


print(eur_to_rub)
