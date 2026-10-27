from pathlib import Path
import string
faili_tee = Path(__file__).with_name("tekst.txt")
with open(faili_tee, encoding="utf-8") as fail:
    sonad = fail.read().split()
puhastatud = [sona.strip(string.punctuation + "„“”«»…—–") for sona in sonad]
puhastatud = [sona for sona in puhastatud if sona]
if puhastatud:
    pikim = max(puhastatud, key=len)
    print("Kõige pikem sõna:", pikim)
    print("Pikkus:", len(pikim))
else:
    print("Failis pole sõnu.")
