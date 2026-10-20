count = 0
summa = 0
positive = 0
negative = 0
even = 0
odd = 0

number = int(input("Sisesta arv (0 lõpetab): "))
while number != 0:
    count += 1
    summa += number
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        pass
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(input("Sisesta arv (0 lõpetab): "))

print("\n--- TULEMUSED ---")
if count == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    print("Sisestatud arve:", count)
    print("Summa:", summa)
    print(f"Keskmine: {summa / count:.2f}")
    print("\nPositiivseid arve:", positive)
    print("Negatiivseid arve:", negative)
    print("Paarisarve:", even)
    print("Paarituid:", odd)
