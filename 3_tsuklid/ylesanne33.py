from random import randint

salajane = randint(1, 100)
arv = int(input("Arva arv 1-100: "))

while arv != salajane:
    if arv > salajane:
        print("Salajane arv on väiksem.")
    else:
        print("Salajane arv on suurem.")
    arv = int(input("Arva arv 1-100: "))

print("Õige!")
