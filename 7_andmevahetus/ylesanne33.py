from pathlib import Path
kaust = Path(__file__).resolve().parent

def loe_nimed(tee):
    with open(tee, encoding="utf-8") as fail:
        return [r.strip() for r in fail if r.strip()]

nimed1 = loe_nimed(kaust / "nimekiri1.txt")
nimed2 = loe_nimed(kaust / "nimekiri2.txt")
uhised = [nimi for nimi in nimed1 if nimi in nimed2]
ainult_esimene = [nimi for nimi in nimed1 if nimi not in nimed2]
ainult_teine = [nimi for nimi in nimed2 if nimi not in nimed1]
print("Mõlemas failis:", uhised)
print("Ainult esimeses failis:", ainult_esimene)
print("Ainult teises failis:", ainult_teine)
