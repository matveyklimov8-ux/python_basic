cpu = float(input("CPU kasutus (%): "))
memory = float(input("Mälu kasutus (%): "))
disk = float(input("Ketta kasutus (%): "))

if cpu > 90 or memory > 90 or disk > 90:
    print("Serveri olek: KRIITILINE")
elif cpu > 75 or memory > 75 or disk > 75:
    print("Serveri olek: HOIATUS")
else:
    print("Serveri olek: OK")