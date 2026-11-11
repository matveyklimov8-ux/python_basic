# Ülesanne 29. Müügiaruande koostamine
from pathlib import Path

kaust = Path(__file__).resolve().parent
read = (kaust / "muuk.txt").read_text(encoding="utf-8").splitlines()
tooted = []

for rea_number, rida in enumerate(read, start=1):
    osad = rida.split()
    if len(osad) != 3:
        print(f"Hoiatus: rida {rea_number} jäeti vahele, sest vorming on vigane.")
        continue
    nimi, hind_tekst, kogus_tekst = osad
    try:
        hind = float(hind_tekst)
        kogus = int(kogus_tekst)
        if hind < 0 or kogus < 0:
            raise ValueError("Hind ja kogus peavad olema mittenegatiivsed.")
    except ValueError as viga:
        print(f"Hoiatus: rida {rea_number} jäeti vahele: {viga}")
        continue
    tooted.append((nimi, hind, kogus, hind * kogus))

if not tooted:
    print("Müügiandmeid ei leitud.")
else:
    aruande_read = ["MÜÜGIARUANNE", "------------------------------"]
    for nimi, hind, kogus, tulu in tooted:
        rea_tekst = f"{nimi}: {kogus} × {hind:.2f} € = {tulu:.2f} €"
        print(rea_tekst)
        # Iga toote müügitulu salvestatakse aruandesse, mitte ainult ekraanile.
        aruande_read.append(rea_tekst)

    kokku = sum(toode[3] for toode in tooted)
    parim = max(tooted, key=lambda toode: toode[3])
    aruande_read.extend([
        "------------------------------",
        f"Kogu müügitulu: {kokku:.2f} €",
        f"Suurima tuluga toode: {parim[0]} ({parim[3]:.2f} €)",
    ])
    aruanne = "\n".join(aruande_read) + "\n"
    print("\n" + aruanne, end="")
    (kaust / "muugiaruanne.txt").write_text(aruanne, encoding="utf-8")
