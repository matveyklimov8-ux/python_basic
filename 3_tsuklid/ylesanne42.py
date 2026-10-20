positive = 0
negative = 0
number = int(input("Sisesta arv (0 lõpetab): "))
while number != 0:
    if number > 0:
        positive += 1
    else:
        negative += 1
    number = int(input("Sisesta arv (0 lõpetab): "))
print("Positiivseid:", positive)
print("Negatiivseid:", negative)
