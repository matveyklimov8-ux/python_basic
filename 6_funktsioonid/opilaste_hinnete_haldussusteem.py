# Kohustuslik kontrollülesanne – Õpilaste hinnete haldussüsteem
# Funktsioonid, järjendid, tingimuslaused, tsüklid ja kontrollitud sisend.

def lisa_opilane(nimed, punktid, nimi, tulemus):
    nimi = nimi.strip()
    if not nimi:
        return False, "Nimi ei tohi olla tühi."
    if any(olemasolev.casefold() == nimi.casefold() for olemasolev in nimed):
        return False, "Sama nimega õpilane on juba olemas."
    if not 0 <= tulemus <= 100:
        return False, "Punktisumma peab olema vahemikus 0–100."
    nimed.append(nimi)
    punktid.append(tulemus)
    return True, "Õpilane lisati."

def arvuta_hinne(punktid):
    if not 0 <= punktid <= 100:
        return None
    if punktid >= 90:
        return 5
    elif punktid >= 75:
        return 4
    elif punktid >= 50:
        return 3
    elif punktid >= 20:
        return 2
    else:
        return 1

def leia_keskmine(punktid):
    if not punktid:
        return None
    summa = 0
    for punkt in punktid:
        summa += punkt
    return summa / len(punktid)

def leia_parim(nimed, punktid):
    if not punktid:
        return None
    parima_indeks = 0
    for i in range(1, len(punktid)):
        if punktid[i] > punktid[parima_indeks]:
            parima_indeks = i
    return nimed[parima_indeks], punktid[parima_indeks]

def leia_norgim(nimed, punktid):
    if not punktid:
        return None
    norgima_indeks = 0
    for i in range(1, len(punktid)):
        if punktid[i] < punktid[norgima_indeks]:
            norgima_indeks = i
    return nimed[norgima_indeks], punktid[norgima_indeks]

def kuva_opilased(nimed, punktid):
    if not nimed:
        print("Õpilasi ei ole veel lisatud.")
        return
    print("\nÕPILASED")
    for i in range(len(nimed)):
        print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti – hinne {arvuta_hinne(punktid[i])}")

def kuva_statistika(nimed, punktid, piir=50):
    if not punktid:
        print("Statistikat ei saa kuvada: õpilaste loend on tühi.")
        return
    parim = leia_parim(nimed, punktid)
    norgim = leia_norgim(nimed, punktid)
    edukad = sum(1 for p in punktid if p >= piir)
    print("\nKLASSI STATISTIKA")
    print("Õpilasi kokku:", len(nimed))
    print(f"Keskmine punktisumma: {leia_keskmine(punktid):.2f}")
    print(f"Parim tulemus: {parim[0]} ({parim[1]} p)")
    print(f"Nõrgim tulemus: {norgim[0]} ({norgim[1]} p)")
    print(f"Vähemalt {piir} punkti: {edukad}")
    print(f"Alla {piir} punkti: {len(punktid) - edukad}")
    print("Hinnete jaotus:")
    for hinne in range(5, 0, -1):
        kogus = sum(1 for p in punktid if arvuta_hinne(p) == hinne)
        print(f"Hinne {hinne}: {kogus} õpilast")

def otsi_opilane(nimed, punktid, nimi):
    otsitav = nimi.strip().casefold()
    for i, olemasolev in enumerate(nimed):
        if olemasolev.casefold() == otsitav:
            return olemasolev, punktid[i]
    return None

def kuva_menuu():
    print("\n=================================")
    print("     ÕPILASTE HINNETE SÜSTEEM")
    print("=================================")
    print("1. Lisa õpilane")
    print("2. Kuva kõik õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("0. Välju")

def kysimus_taisarv(tekst):
    while True:
        try:
            return int(input(tekst))
        except ValueError:
            print("Palun sisesta täisarv.")

def main():
    nimed = []
    punktid = []
    while True:
        kuva_menuu()
        valik = input("Vali tegevus: ").strip()
        if valik == "1":
            nimi = input("Õpilase nimi: ")
            tulemus = kysimus_taisarv("Punktisumma (0–100): ")
            lisatud, teade = lisa_opilane(nimed, punktid, nimi, tulemus)
            print(teade)
        elif valik == "2":
            kuva_opilased(nimed, punktid)
        elif valik == "3":
            kuva_statistika(nimed, punktid)
        elif valik == "4":
            nimi = input("Sisesta otsitava õpilase nimi: ")
            leitud = otsi_opilane(nimed, punktid, nimi)
            if leitud is None:
                print("Sellist õpilast ei leitud.")
            else:
                print("Õpilane:", leitud[0])
                print("Punktid:", leitud[1])
                print("Hinne:", arvuta_hinne(leitud[1]))
        elif valik == "0":
            print("Programm lõpetas töö.")
            break
        else:
            print("Vigane valik. Proovi uuesti.")

if __name__ == "__main__":
    main()
