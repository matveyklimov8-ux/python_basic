from pathlib import Path
arvud = []
for i in range(1, 6):
    arvud.append(int(input(f"Sisesta {i}. täisarv: ")))
faili_tee = Path(__file__).with_name("sisestatud_arvud.txt")
with open(faili_tee, "w", encoding="utf-8") as fail:
    for arv in arvud:
        fail.write(f"{arv}\n")
with open(faili_tee, encoding="utf-8") as fail:
    loetud = [int(r.strip()) for r in fail if r.strip()]
print("Sisestatud arvud:", ", ".join(map(str, loetud)))
print("Summa:", sum(loetud))
print("Keskmine:", sum(loetud) / len(loetud) if loetud else 0)
