from random import randint
heads = 0
letters = 0
i = 0
while i < 100:
    result = randint(1, 2)
    if result == 1:
        heads += 1
    else:
        letters += 1
    i += 1
print("Kull:", heads)
print("Kiri:", letters)
print("Kokku:", heads + letters)
