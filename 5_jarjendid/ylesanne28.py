# Ülesanne 28. Arvude summa failist
from pathlib import Path
faili_tee = Path(__file__).with_name("arvud.txt")
summa = 0
arvude_arv = 0
with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida:
            summa += int(rida)
            arvude_arv += 1
print("Arvude arv:", arvude_arv)
print("Arvude summa:", summa)
