from pathlib import Path
kaust = Path(__file__).resolve().parent
with open(kaust / "arvud.txt", encoding="utf-8") as fail:
    arvud = [int(r.strip()) for r in fail if r.strip()]
paarisarvud = [arv for arv in arvud if arv % 2 == 0]
with open(kaust / "paarisarvud.txt", "w", encoding="utf-8") as fail:
    for arv in paarisarvud:
        fail.write(f"{arv}\n")
print("Uude faili kirjutati", len(paarisarvud), "paarisarvu.")
