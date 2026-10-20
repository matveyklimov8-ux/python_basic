# Ülesanne 48. Poe ostukorv

def lisa_toode(tooted, hinnad, kogused, nimi, hind, kogus):
    tooted.append(nimi)
    hinnad.append(hind)
    kogused.append(kogus)

def rea_maksumus(hind, kogus):
    return hind * kogus

def kogu_summa(hinnad, kogused):
    summa = 0
    for i in range(len(hinnad)):
        summa += rea_maksumus(hinnad[i], kogused[i])
    return summa

def kuva_ostukorv(tooted, hinnad, kogused):
    for i in range(len(tooted)):
        print(f"{tooted[i]} x {kogused[i]} – {rea_maksumus(hinnad[i], kogused[i]):.2f} €")
    print(f"Kokku: {kogu_summa(hinnad, kogused):.2f} €")

tooted, hinnad, kogused = [], [], []
while True:
    nimi = input("Toote nimi (lõpetamiseks ENTER): ").strip()
    if not nimi:
        break
    try:
        hind = float(input("Hind (€): "))
        kogus = int(input("Kogus: "))
        if hind < 0 or kogus <= 0:
            print("Hind peab olema vähemalt 0 ja kogus positiivne.")
            continue
    except ValueError:
        print("Vigane hind või kogus.")
        continue
    lisa_toode(tooted, hinnad, kogused, nimi, hind, kogus)

kuva_ostukorv(tooted, hinnad, kogused)
