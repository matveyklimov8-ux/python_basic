from random import randint
secret = randint(1, 10)
guess = int(input("Arva arv 1–10: "))
while guess != secret:
    print("Vale!")
    guess = int(input("Arva arv 1–10: "))
print("Õige!")
