# Ülesanne 27. Faili sisu väljastamine
from pathlib import Path
faili_tee = Path(__file__).with_name("linnad.txt")
linnad = []
with open(faili_tee, encoding="utf-8") as fail:
    for rida in fail:
        linn = rida.strip()
        if linn:
            linnad.append(linn)
for linn in linnad:
    print(linn)
print("Linnu kokku:", len(linnad))
