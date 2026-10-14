# Ülesanne 30. Temperatuuride analüüs
from pathlib import Path
faili_tee = Path(__file__).with_name("temperatuurid.txt")
with open(faili_tee, encoding="utf-8") as fail:
    temperatuurid = [int(rida.strip()) for rida in fail if rida.strip()]
alla_nulli = sum(1 for t in temperatuurid if t < 0)
vahemalt_viis = sum(1 for t in temperatuurid if t >= 5)
print("Mõõtmisi:", len(temperatuurid))
print(f"Keskmine temperatuur: {sum(temperatuurid) / len(temperatuurid):.1f} °C")
print("Kõrgeim temperatuur:", max(temperatuurid), "°C")
print("Madalaim temperatuur:", min(temperatuurid), "°C")
print("Miinuskraadidega päevi:", alla_nulli)
print("Vähemalt 5-kraadiseid päevi:", vahemalt_viis)
