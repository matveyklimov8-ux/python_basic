from random import randint

salajane = randint(1, 100)
katse = 1
arvatud = False

while katse <= 7 and not arvatud:
    arv = int(input("Arva arv 1-100: "))

    if arv == salajane:
        print("Õige! Võitsid!")
        arvatud = True
    elif arv > salajane:
        print("Salajane arv on väiksem.")
    else:
        print("Salajane arv on suurem.")

    katse = katse + 1

if not arvatud:
    print("Kahjuks kaotasid.")
    print("Õige arv oli", salajane)
