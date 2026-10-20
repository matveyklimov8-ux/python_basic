count = 0
summa = 0.0
temperature = float(input("Sisesta temperatuur (999 lõpetab): "))
while temperature != 999:
    summa += temperature
    count += 1
    temperature = float(input("Sisesta temperatuur (999 lõpetab): "))
if count > 0:
    print("Temperatuure:", count)
    print("Summa:", summa)
    print("Keskmine:", summa / count)
else:
    print("Temperatuure ei sisestatud.")
