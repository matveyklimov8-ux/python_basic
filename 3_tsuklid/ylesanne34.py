from random import randint
secret = randint(1, 100)
attempts = 0
guess = None
while guess != secret:
    guess = int(input("Arva arv 1–100: "))
    attempts += 1
    if guess < secret:
        print("Salajane arv on suurem.")
    elif guess > secret:
        print("Salajane arv on väiksem.")
print("Õige!")
print("Arvasid arvu ära", attempts, "katsega.")
