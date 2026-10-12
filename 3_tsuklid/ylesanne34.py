from random import randint

salajane = randint(1, 100)
katseid = 0
arv = 0

while arv != salajane:
    arv = int(input("Arva arv 1-100: "))
    katseid = katseid + 1
    if arv > salajane:
        print("Salajane arv on väiksem.")
    elif arv < salajane:
        print("Salajane arv on suurem.")

print("Õige!")
print("Arvasid arvu ära", katseid, "katsega.")
