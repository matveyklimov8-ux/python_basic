from pathlib import Path
kaust = Path(__file__).resolve().parent
kehtivad, vigased = [], 0
with open(kaust / "mootmised.txt", encoding="utf-8") as fail:
    for rida in fail:
        sisu = rida.strip()
        if not sisu:
            continue
        try:
            kehtivad.append(float(sisu))
        except ValueError:
            vigased += 1
print("Kehtivaid arvväärtusi:", len(kehtivad))
print("Vigaseid kirjeid:", vigased)
if kehtivad:
    print(f"Keskmine: {sum(kehtivad) / len(kehtivad):.2f}")
else:
    print("Keskmist ei saa arvutada, sest kehtivaid väärtusi pole.")
(kaust / "korrektsed_mootmised.txt").write_text("".join(f"{x:g}\n" for x in kehtivad), encoding="utf-8")
