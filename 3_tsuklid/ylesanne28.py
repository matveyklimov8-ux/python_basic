from random import randint
i = 1
summa = 0
while i <= 10:
    roll = randint(1, 6)
    print(f"{i}. vise: {roll}")
    summa += roll
    i += 1
print("Visete summa:", summa)
print("Keskmine tulemus:", summa / 10)
