from pathlib import Path
faili_tee = Path(__file__).with_name("arvud.txt")
with open(faili_tee, encoding="utf-8") as fail:
    arvud = [int(rida.strip()) for rida in fail if rida.strip()]
print("Arvud:", arvud)
print("Summa:", sum(arvud))
