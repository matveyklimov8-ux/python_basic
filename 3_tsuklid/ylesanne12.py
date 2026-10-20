count = int(input("Mitu arvu soovid sisestada? "))
i = 0
summa = 0.0
while i < count:
    summa += float(input("Sisesta arv: "))
    i += 1
if count > 0:
    print("Summa:", summa)
    print("Keskmine:", summa / count)
else:
    print("Arve ei sisestatud.")
