# Ülesanne 35. Spordivõistluse tulemused
from pathlib import Path
faili_tee = Path(__file__).with_name("tulemused.csv")
nimed = []
tulemused = []
with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            nimi, tulemus = rida.split(";")
            nimed.append(nimi)
            tulemused.append(float(tulemus))
for nimi, tulemus in zip(nimed, tulemused):
    print(f"{nimi}: {tulemus:.1f} m")
parim = max(tulemused)
print(f"Parim tulemus: {nimed[tulemused.index(parim)]} – {parim:.1f} m")
keskmine = sum(tulemused) / len(tulemused)
print(f"Keskmine tulemus: {keskmine:.2f} m")
print("Keskmisest paremad:")
for nimi, tulemus in zip(nimed, tulemused):
    if tulemus > keskmine:
        print(f"{nimi}: {tulemus:.1f} m")
