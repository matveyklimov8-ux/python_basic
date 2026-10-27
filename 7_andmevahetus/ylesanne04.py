from pathlib import Path
faili_tee = Path(__file__).with_name("nimed.txt")
with open(faili_tee, encoding="utf-8") as fail:
    nimed = [rida.strip() for rida in fail if rida.strip()]
if nimed:
    print("Esimene nimi:", nimed[0])
    print("Viimane nimi:", nimed[-1])
else:
    print("Failis pole nimesid.")
