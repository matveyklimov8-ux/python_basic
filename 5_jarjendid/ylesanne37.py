# Ülesanne 37. Tekstifaili analüsaator
from pathlib import Path
faili_tee = Path(__file__).with_name("tekst.txt")
with open(faili_tee, encoding="utf-8") as fail:
    read = [rida.rstrip("\r\n") for rida in fail]
sonad = []
tihte_kokku = sum(len(rida) for rida in read)
for rida in read:
    sonad.extend(rida.split())
pikim_rida = max(read, key=len) if read else ""
puhastatud_sonad = [sona.strip(".,!?;:\"'()[]{}") for sona in sonad]
puhastatud_sonad = [sona for sona in puhastatud_sonad if sona]
pikim_sona = max(puhastatud_sonad, key=len) if puhastatud_sonad else ""
pythoniga_read = sum(1 for rida in read if "python" in rida.lower())
print("Ridu:", len(read))
print("Tähemärke (ilma reavahetusteta):", tihte_kokku)
print("Sõnu kokku:", len(sonad))
print("Kõige pikem rida:", pikim_rida)
print("Kõige pikem sõna:", pikim_sona)
print("Ridu, kus esineb sõna Python:", pythoniga_read)
