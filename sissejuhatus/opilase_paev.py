name = input("Nimi: ")
age = int(input("Vanus: "))
distance = float(input("Koolitee: "))
minutes = int(input("Aeg minutites: "))

next_age = age + 1
meters = int(distance * 1000)

hours = minutes // 60
minutes_left = minutes % 60

speed = distance / (minutes / 60)

print("Tere,", name + "!")
print("Järgmisel aastal oled " + str(next_age) + "-aastane.")
print("Sinu koolitee pikkus on", meters, "meetrit.")
print("Koolitee kestab", hours, "tundi ja", minutes_left, "minutit.")
print("Keskmine kiirus on", speed, "km/h.")