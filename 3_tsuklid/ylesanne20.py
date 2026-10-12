summa = 1000
aasta = 1

while aasta <= 10:
    summa = summa * 1.05
    print(str(aasta) + ". aasta:", round(summa, 2), "eurot")
    aasta = aasta + 1
