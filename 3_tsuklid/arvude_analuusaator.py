# Kohustuslik kontrollulesanne: arvude analüsaator
arvude_kogus = 0
summa = 0
positiivseid = 0
negatiivseid = 0
paarisarve = 0
paarituid = 0

arv = int(input("Sisesta arv (0 lõpetab): "))

while arv != 0:
    arvude_kogus = arvude_kogus + 1
    summa = summa + arv

    if arv > 0:
        positiivseid = positiivseid + 1
    elif arv < 0:
        negatiivseid = negatiivseid + 1
    else:
        pass  # 0 lõpetab tsukli enne statistika uuendamist.

    if arv % 2 == 0:
        paarisarve = paarisarve + 1
    else:
        paarituid = paarituid + 1

    arv = int(input("Sisesta arv (0 lõpetab): "))

print("--- TULEMUSED ---")

if arvude_kogus == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    print("Sisestatud arve:", arvude_kogus)
    print("Summa:", summa)
    print("Keskmine: %.2f" % (summa / arvude_kogus))
    print("Positiivseid arve:", positiivseid)
    print("Negatiivseid arve:", negatiivseid)
    print("Paarisarve:", paarisarve)
    print("Paarituid:", paarituid)
