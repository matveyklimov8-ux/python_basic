from pathlib import Path
kaust = Path(__file__).resolve().parent
sisend = kaust / "algtekst.txt"
valjund = kaust / "suured_tahed.txt"
with open(sisend, encoding="utf-8") as fail:
    tekst = fail.read()
with open(valjund, "w", encoding="utf-8") as fail:
    fail.write(tekst.upper())
print("Suurtähtedega tekst salvestati faili suured_tahed.txt.")
