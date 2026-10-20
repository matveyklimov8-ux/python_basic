age = int(input("Vanus: "))
student = input("Kas oled õpilane (jah/ei): ").strip().lower()
if age < 7:
    price = 0
elif age <= 17:
    price = 5
elif age >= 65:
    price = 6
elif student == "jah":
    price = 8
else:
    price = 12
print("Pileti hind:", price, "€")
