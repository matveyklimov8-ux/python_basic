# Ülesanne 36. Lihtne ostukorv
tooted = []
hinnad = []
while True:
    nimi = input("Sisesta toote nimi (lõpetamiseks ENTER): ").strip()
    if nimi == "":
        break
    hind = float(input("Sisesta hind eurodes: "))
    tooted.append(nimi)
    hinnad.append(hind)
print("\nOSTUKORV")
for nimi, hind in zip(tooted, hinnad):
    print(f"{nimi} – {hind:.2f} €")
print("Tooteid kokku:", len(tooted))
summa = sum(hinnad)
print(f"Kogumaksumus: {summa:.2f} €")
if hinnad:
    indeks = hinnad.index(max(hinnad))
    print(f"Kõige kallim toode: {tooted[indeks]} ({hinnad[indeks]:.2f} €)")
    soodustus = float(input("Allahindlus protsentides (0–100): "))
    if 0 <= soodustus <= 100:
        print(f"Hind pärast allahindlust: {summa * (1 - soodustus / 100):.2f} €")
    else:
        print("Allahindlus peab jääma vahemikku 0–100%.")
else:
    print("Ostukorv on tühi.")
