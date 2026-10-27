from pathlib import Path
kaust = Path(__file__).resolve().parent
with open(kaust / "temperatuurid.txt", encoding="utf-8") as fail:
    andmed = []
    for rida in fail:
        osad = rida.split()
        if len(osad) == 2:
            andmed.append((osad[0], float(osad[1])))
if not andmed:
    print("Temperatuuriandmeid ei leitud.")
else:
    keskmine = sum(t for _, t in andmed) / len(andmed)
    soojem = max(andmed, key=lambda x: x[1])
    kylmem = min(andmed, key=lambda x: x[1])
    ule_15 = sum(1 for _, t in andmed if t > 15)
    aruanne = (f"Nädala keskmine temperatuur: {keskmine:.2f} °C\n"
               f"Kõige soojem päev: {soojem[0]} ({soojem[1]:g} °C)\n"
               f"Kõige külmem päev: {kylmem[0]} ({kylmem[1]:g} °C)\n"
               f"Päevi üle 15 kraadi: {ule_15}\n")
    print(aruanne, end="")
    (kaust / "temperatuuri_aruanne.txt").write_text(aruanne, encoding="utf-8")
