from pathlib import Path
faili_tee = Path(__file__).with_name("tooted.txt")
otsitav = input("Sisesta toode: ").strip().casefold()
with open(faili_tee, encoding="utf-8") as fail:
    tooted = [rida.strip() for rida in fail if rida.strip()]
if any(toode.casefold() == otsitav for toode in tooted):
    print("Toode leiti nimekirjast.")
else:
    print("Toodet ei leitud nimekirjast.")
