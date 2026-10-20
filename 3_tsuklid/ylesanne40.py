count = 0
summa = 0.0
price = float(input("Sisesta hind (0 lõpetab): "))
while price != 0:
    if price > 0:
        summa += price
        count += 1
    else:
        print("Hind peab olema positiivne või 0 lõpetamiseks.")
    price = float(input("Sisesta hind (0 lõpetab): "))
print("Tooteid:", count)
print(f"Kokku: {summa:.2f} €")
