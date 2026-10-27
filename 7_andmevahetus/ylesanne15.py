nimi = input("Nimi: ").strip()
vanus = input("Vanus: ").strip()
epost = input("E-posti aadress: ").strip()
from pathlib import Path
faili_tee = Path(__file__).with_name("kasutaja.txt")
with open(faili_tee, "w", encoding="utf-8") as fail:
    fail.write(f"{nimi}\n{vanus}\n{epost}\n")
print("Andmed salvestati faili. Faili sisu:")
with open(faili_tee, encoding="utf-8") as fail:
    print(fail.read(), end="")
