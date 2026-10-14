# Ülesanne 29. Arvude salvestamine järjendisse
from pathlib import Path
faili_tee = Path(__file__).with_name("arvud.txt")
with open(faili_tee, encoding="utf-8") as fail:
    arvud = [int(rida.strip()) for rida in fail if rida.strip()]
print("Arvud:", arvud)
print("Suurim:", max(arvud))
print("Väikseim:", min(arvud))
print("Keskmine:", sum(arvud) / len(arvud))
print("Kasvavas järjekorras:", sorted(arvud))
