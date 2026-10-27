from pathlib import Path
faili_tee = Path(__file__).with_name("arvud.txt")
with open(faili_tee, encoding="utf-8") as fail:
    arvud = [int(r.strip()) for r in fail if r.strip()]
paaris = sum(1 for arv in arvud if arv % 2 == 0)
paaritu = sum(1 for arv in arvud if arv % 2 != 0)
print("Paarisarve:", paaris)
print("Paarituid arve:", paaritu)
