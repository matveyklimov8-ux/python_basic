from random import randint

vise = 1
kull = 0
kiri = 0

while vise <= 100:
    tulemus = randint(1, 2)
    if tulemus == 1:
        kull = kull + 1
    else:
        kiri = kiri + 1
    vise = vise + 1

print("Kull:", kull)
print("Kiri:", kiri)
print("Kokku:", kull + kiri)
