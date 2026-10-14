# Ülesanne 22. Järjendi elementide muutmine
hinnad = [12.50, 8.90, 25.00, 4.75, 19.99]
for indeks in range(len(hinnad)):
    hinnad[indeks] = hinnad[indeks] * 1.10
print("Uuendatud hinnad:")
for hind in hinnad:
    print(f"{hind:.2f} €")
