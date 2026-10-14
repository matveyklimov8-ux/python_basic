# Ülesanne 31. Nimede otsimine failist
from pathlib import Path
faili_tee = Path(__file__).with_name("opilased.txt")
with open(faili_tee, encoding="utf-8") as fail:
    nimed = [rida.strip() for rida in fail if rida.strip()]
otsitav = input("Sisesta otsitav nimi: ").strip().casefold()
leitud = False
for indeks, nimi in enumerate(nimed, start=1):
    if nimi.casefold() == otsitav:
        print("Nimi leiti.")
        print("Järjekorranumber:", indeks)
        leitud = True
        break
if not leitud:
    print("Nime ei leitud.")
