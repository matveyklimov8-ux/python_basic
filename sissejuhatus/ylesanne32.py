distance = float(input("Teepikkus kilomeetrites: "))
time = float(input("Aeg tundides: "))
if time > 0:
    print("Keskmine kiirus:", distance / time, "km/h")
else:
    print("Aeg peab olema suurem kui 0.")
