from pathlib import Path
import re
from collections import Counter
faili_nimi = input("Analüüsitava tekstifaili nimi: ").strip()
try:
    tekst = Path(faili_nimi).read_text(encoding="utf-8")
except FileNotFoundError:
    print("Viga: faili ei leitud.")
else:
    sonad = re.findall(r"[^\W\d_]+(?:['’][^\W\d_]+)?", tekst.casefold(), flags=re.UNICODE)
    laused = [osa for osa in re.split(r"[.!?]+", tekst) if osa.strip()]
    pikim = max(sonad, key=len) if sonad else ""
    sagedus = Counter(sonad).most_common(5)
    read = [f"Sõnade arv: {len(sonad)}", f"Lausete ligikaudne arv: {len(laused)}", f"Pikim sõna: {pikim}", "Viis sagedasemat sõna:"]
    read += [f"{sona}: {arv}" for sona, arv in sagedus]
    aruanne = "\n".join(read) + "\n"
    print(aruanne, end="")
    Path(__file__).with_name("tekstianaluus.txt").write_text(aruanne, encoding="utf-8")
