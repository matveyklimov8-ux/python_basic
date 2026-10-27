from pathlib import Path
kaust = Path(__file__).resolve().parent
read = (kaust / "muuk.txt").read_text(encoding="utf-8").splitlines()
tooted = []
for rida in read:
    osad = rida.split()
    if len(osad) == 3:
        nimi, hind, kogus = osad[0], float(osad[1]), int(osad[2])
        tooted.append((nimi, hind, kogus, hind * kogus))
if not tooted:
    print("Müügiandmeid ei leitud.")
else:
    for nimi, hind, kogus, tulu in tooted:
        print(f"{nimi}: {kogus} × {hind:.2f} € = {tulu:.2f} €")
    kokku = sum(r[3] for r in tooted)
    parim = max(tooted, key=lambda r: r[3])
    aruanne = "Kogu müügitulu: {:.2f} €\nSuurima tuluga toode: {} ({:.2f} €)\n".format(kokku, parim[0], parim[3])
    print(aruanne, end="")
    (kaust / "muugiaruanne.txt").write_text(aruanne, encoding="utf-8")
