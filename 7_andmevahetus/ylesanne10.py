from pathlib import Path
faili_tee = Path(__file__).with_name("tekst.txt")
with open(faili_tee, encoding="utf-8") as fail:
    tekst = fail.read()
sonad = tekst.split()
print("Tekstis on", len(sonad), "sõna.")
# Moodle'i näidistekstis on tegelikult 13 sõna; arvutame faili tegeliku sisu põhjal.
