# Ülesanne 32. CSV-faili töötlemine
from pathlib import Path
faili_tee = Path(__file__).with_name("tooted.csv")
tooted = []
hinnad = []
with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            nimi, hind = rida.split(";")
            tooted.append(nimi)
            hinnad.append(float(hind))
for nimi, hind in zip(tooted, hinnad):
    print(f"{nimi} – {hind:.2f} €")
if tooted:
    kalleima_indeks = hinnad.index(max(hinnad))
    print("Tooteid kokku:", len(tooted))
    print(f"Kogumaksumus: {sum(hinnad):.2f} €")
    print(f"Kõige kallim toode: {tooted[kalleima_indeks]} ({hinnad[kalleima_indeks]:.2f} €)")
