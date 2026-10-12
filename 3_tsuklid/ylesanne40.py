summa = 0
kogus = 0

while True:
    hind = float(input("Sisesta hind: "))
    if hind == 0:
        break
    summa = summa + hind
    kogus = kogus + 1

print("Tooteid:", kogus)
print("Kokku: %.2f €" % summa)
