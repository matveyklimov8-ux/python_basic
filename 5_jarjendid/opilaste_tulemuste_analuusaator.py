# KOHUSTUSLIK: Õpilaste tulemuste analüsaator
from pathlib import Path

faili_tee = Path(__file__).with_name("kontrolltoo.csv")
nimed = []
punktid = []

with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            nimi, punktide_tekst = rida.split(";")
            nimed.append(nimi)
            punktid.append(int(punktide_tekst))

def leia_hinne(punktid_summa):
    if punktid_summa >= 90:
        return 5
    elif punktid_summa >= 75:
        return 4
    elif punktid_summa >= 50:
        return 3
    elif punktid_summa >= 20:
        return 2
    else:
        return 1

print("KONTROLLTÖÖ TULEMUSED")
for indeks in range(len(nimed)):
    print(f"{indeks + 1}. {nimed[indeks]} – {punktid[indeks]} punkti")

korgeim = max(punktid)
madalaim = min(punktid)
parimad = [nimed[i] for i in range(len(nimed)) if punktid[i] == korgeim]
halvimad = [nimed[i] for i in range(len(nimed)) if punktid[i] == madalaim]
sooritas = sum(1 for punkt in punktid if punkt >= 50)
ei_sooritanud = sum(1 for punkt in punktid if punkt < 50)
print("\nKONTROLLTÖÖ STATISTIKA")
print("Õpilasi kokku:", len(nimed))
print(f"Keskmine punktisumma: {sum(punktid) / len(punktid):.1f}")
print(f"Parim tulemus: {', '.join(parimad)} – {korgeim} punkti")
print(f"Madalaim tulemus: {', '.join(halvimad)} – {madalaim} punkti")
print("Kontrolltöö sooritas:", sooritas, "õpilast")
print("Kontrolltööd ei sooritanud:", ei_sooritanud, "õpilast")

print("\nHINDED")
for nimi, punkt in zip(nimed, punktid):
    print(f"{nimi} – {punkt} punkti – hinne {leia_hinne(punkt)}")

print("\nÕPILASE OTSIMINE")
otsitav = input("Sisesta õpilase nimi: ").strip().casefold()
leitud = False
for nimi, punkt in zip(nimed, punktid):
    if nimi.casefold() == otsitav:
        print("Õpilane:", nimi)
        print("Punktid:", punkt)
        print("Hinne:", leia_hinne(punkt))
        leitud = True
        break
if not leitud:
    print("Sellist õpilast ei leitud.")
