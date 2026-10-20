from random import randint
heads = 0
letters = 0
i = 0
while i < 1000:
    if randint(1, 10) <= 7:
        letters += 1  # Kiri 70% tõenäosusega
    else:
        heads += 1
    i += 1
print("Kiri:", letters)
print("Kull:", heads)
