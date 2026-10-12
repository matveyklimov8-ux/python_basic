kogus = int(input("Mitu arvu soovid sisestada? "))
i = 0
summa = 0

while i < kogus:
    arv = float(input("Sisesta arv: "))
    summa = summa + arv
    i = i + 1

if kogus > 0:
    keskmine = summa / kogus
    print("Summa:", summa)
    print("Keskmine:", keskmine)
else:
    print("Ühtegi arvu ei sisestatud.")
