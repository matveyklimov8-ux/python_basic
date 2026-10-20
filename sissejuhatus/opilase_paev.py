name = input("Nimi: ")
age = int(input("Vanus: "))
distance_km = float(input("Koolitee pikkus kilomeetrites: "))
time_minutes = int(input("Koolitee kestus minutites: "))
print(f"Tere, {name}!")
print(f"Järgmisel aastal oled {age + 1}-aastane.")
print("Sinu koolitee pikkus on", distance_km * 1000, "meetrit.")
print("Koolitee kestab", time_minutes // 60, "tundi ja", time_minutes % 60, "minutit.")
if time_minutes > 0:
    speed = distance_km / (time_minutes / 60)
    print("Keskmine kiirus on", round(speed, 2), "km/h.")
else:
    print("Keskmist kiirust ei saa arvutada, sest aeg peab olema positiivne.")
