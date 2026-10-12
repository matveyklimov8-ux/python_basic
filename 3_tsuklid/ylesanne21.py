summa = 1000
aasta = 0

while summa < 2000:
    summa = summa * 1.05
    aasta = aasta + 1

print("Aastaid kulus:", aasta)
print("Summa:", round(summa, 2), "eurot")
