distance = float(input("Läbitud kilomeetrid: "))
litres = float(input("Kasutatud kütus liitrites: "))
if distance > 0:
    print("Kütusekulu:", litres / distance * 100, "l/100 km")
else:
    print("Läbitud kilomeetrid peavad olema suuremad kui 0.")
