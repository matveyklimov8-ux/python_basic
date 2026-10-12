kogus = 0
summa = 0

while True:
    temperatuur = float(input("Sisesta temperatuur (999 lõpetab): "))
    if temperatuur == 999:
        break
    summa = summa + temperatuur
    kogus = kogus + 1

if kogus > 0:
    print("Temperatuure sisestati:", kogus)
    print("Temperatuuride summa:", summa)
    print("Keskmine temperatuur:", summa / kogus)
else:
    print("Ühtegi temperatuuri ei sisestatud.")
