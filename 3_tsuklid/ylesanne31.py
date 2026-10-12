from random import randint

vise = 1
kiri = 0
kull = 0

while vise <= 1000:
    tulemus = randint(1, 100)
    if tulemus <= 70:
        kiri = kiri + 1
    else:
        kull = kull + 1
    vise = vise + 1

print("Kiri:", kiri)
print("Kull:", kull)
