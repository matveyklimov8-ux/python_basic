# Ülesanne 9. Järjendi täiendamine
ostukorv = []
for i in range(5):
    toode = input(f"Sisesta {i + 1}. toote nimi: ")
    ostukorv.append(toode)
print("Ostukorv:", ostukorv)
print("Tooteid kokku:", len(ostukorv))
