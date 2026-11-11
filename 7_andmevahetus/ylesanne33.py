# Ülesanne 33. Kahe faili võrdlemine ja tulemuste salvestamine
from pathlib import Path

kaust = Path(__file__).resolve().parent

def loe_nimed(tee):
    with open(tee, encoding="utf-8") as fail:
        return [r.strip() for r in fail if r.strip()]


def koosta_vordlus(nimed1, nimed2):
    uhised = [nimi for nimi in nimed1 if nimi in nimed2]
    ainult_esimene = [nimi for nimi in nimed1 if nimi not in nimed2]
    ainult_teine = [nimi for nimi in nimed2 if nimi not in nimed1]

    return (
        f"Mõlemas failis: {uhised}\n"
        f"Ainult esimeses failis: {ainult_esimene}\n"
        f"Ainult teises failis: {ainult_teine}\n"
    )


nimed1 = loe_nimed(kaust / "nimekiri1.txt")
nimed2 = loe_nimed(kaust / "nimekiri2.txt")
aruanne = koosta_vordlus(nimed1, nimed2)
print(aruanne, end="")

# Võrdluse tulemus salvestatakse nõutud faili comparison.txt.
(kaust / "comparison.txt").write_text(aruanne, encoding="utf-8")
