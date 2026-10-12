from random import randint

vise = 1
kuute = 0

while vise <= 100:
    tulemus = randint(1, 6)
    if tulemus == 6:
        kuute = kuute + 1
    vise = vise + 1

print("Täringut visati 100 korda.")
print("Kuus saadi", kuute, "korda.")
