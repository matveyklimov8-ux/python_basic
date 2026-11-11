# Ülesanne 27. Veebist faili salvestamine ja salvestatud faili lugemine
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
kaust = Path(__file__).resolve().parent
salvestus = kaust / "veebitekst.txt"

try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")

    # Kõigepealt kirjutame allalaaditud teksti kohalikku faili.
    salvestus.write_text(tekst, encoding="utf-8")

    # Seejärel avame just salvestatud faili uuesti, et kontrollida failiga töötamist.
    salvestatud_tekst = salvestus.read_text(encoding="utf-8")
    read = salvestatud_tekst.splitlines()

    print("Allalaadimine ja faili salvestamine õnnestus.")
    if read:
        print("Esimene rida:", read[0])
        print("Viimane rida:", read[-1])
    else:
        print("Salvestatud fail on tühi.")
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError, OSError) as viga:
    print("Allalaadimine või faili töötlemine ebaõnnestus:", viga)
