from random import randint
secret = randint(1, 100)
guess = int(input("Arva arv 1–100: "))
while guess != secret:
    if guess < secret:
        print("Salajane arv on suurem.")
    else:
        print("Salajane arv on väiksem.")
    guess = int(input("Arva arv 1–100: "))
print("Õige!")
