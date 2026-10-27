from pathlib import Path
faili_tee = Path(__file__).with_name("opilased.txt")
tulemused = []
with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) >= 2:
            nimi = osad[0]
            hinded = [int(x) for x in osad[1:]]
            tulemused.append((nimi, hinded))
for nimi, hinded in tulemused:
    print(f"{nimi}: hinnete arv {len(hinded)}, keskmine {sum(hinded) / len(hinded):.2f}")
if tulemused:
    nimi, hinded = max(tulemused, key=lambda tulemus: len(tulemus[1]))
    print(f"Kõige rohkem hindeid: {nimi} ({len(hinded)})")
