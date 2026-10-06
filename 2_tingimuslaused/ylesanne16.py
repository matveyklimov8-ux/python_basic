age = int(input("Sisesta vanus: "))

if age < 18 or age >= 65:
    print("Pileti hind: 6 eurot")
else:
    print("Pileti hind: 10 eurot")