from random import randint
secret = randint(1, 100)
attempts = 0
won = False
while attempts < 7 and not won:
    guess = int(input("Arva arv 1–100: "))
    attempts += 1
    if guess == secret:
        won = True
    elif guess < secret:
        print("Salajane arv on suurem.")
    else:
        print("Salajane arv on väiksem.")
if won:
    print("Õige! Võitsid!")
else:
    print("Kahjuks kaotasid.")
    print("Õige arv oli", secret)
