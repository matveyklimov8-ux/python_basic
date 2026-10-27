from pathlib import Path
kaust = Path(__file__).resolve().parent
sisendfail = kaust / "tulemused.txt"
valjundfail = kaust / "aruanne.txt"
def hinne(keskmine):
    if keskmine >= 90: return 5
    if keskmine >= 75: return 4
    if keskmine >= 60: return 3
    if keskmine >= 50: return 2
    return 1
try:
    opilased = []
    with open(sisendfail, encoding="utf-8") as fail:
        for nr, rida in enumerate(fail, start=1):
            osad = rida.strip().split(";")
            if not rida.strip():
                continue
            if len(osad) != 4:
                print(f"Hoiatus: rida {nr} jäeti vahele (oodati nime ja kolme tulemust).")
                continue
            nimi = osad[0].strip()
            try:
                punktid = [int(x) for x in osad[1:]]
            except ValueError:
                print(f"Hoiatus: rida {nr} jäeti vahele (punktid pole täisarvud).")
                continue
            if not nimi or any(p < 0 or p > 100 for p in punktid):
                print(f"Hoiatus: rida {nr} jäeti vahele (vigased andmed).")
                continue
            keskmine = sum(punktid) / len(punktid)
            opilased.append((nimi, punktid, keskmine, hinne(keskmine)))
except FileNotFoundError:
    print("Viga: faili tulemused.txt ei leitud. Lisa see 7_andmevahetus kausta.")
    raise SystemExit(1)
if not opilased:
    print("Viga: failis pole korrektseid õpilaste tulemusi.")
    raise SystemExit(1)
ridade_keskmised = [o[2] for o in opilased]
parim_keskmine = max(ridade_keskmised)
norgim_keskmine = min(ridade_keskmised)
aruande_read = ["ÕPILASTE TULEMUSTE ARUANNE", "------------------------------", ""]
for nimi, punktid, keskmine, hinne_nr in opilased:
    aruande_read.append(f"{nimi:<10} Keskmine: {keskmine:5.2f}  Hinne: {hinne_nr}")
aruande_read += ["", "------------------------------", f"Klassi keskmine: {sum(ridade_keskmised) / len(ridade_keskmised):.2f}"]
aruande_read.append("Parim õpilane: " + ", ".join(o[0] for o in opilased if o[2] == parim_keskmine))
aruande_read.append("Nõrgim õpilane: " + ", ".join(o[0] for o in opilased if o[2] == norgim_keskmine))
aruande_read.append(f"Positiivse hindega õpilasi: {sum(1 for o in opilased if o[3] >= 3)}")
aruanne = "\n".join(aruande_read) + "\n"
print(aruanne, end="")
valjundfail.write_text(aruanne, encoding="utf-8")
print("Aruanne salvestati faili aruanne.txt.")
