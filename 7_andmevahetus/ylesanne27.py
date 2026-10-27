from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
kaust = Path(__file__).resolve().parent
salvestus = kaust / "veebitekst.txt"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    salvestus.write_text(tekst, encoding="utf-8")
    read = tekst.splitlines()
    print("Allalaadimine õnnestus.")
    if read:
        print("Esimene rida:", read[0])
        print("Viimane rida:", read[-1])
    else:
        print("Fail on tühi.")
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError, OSError) as viga:
    print("Allalaadimine ebaõnnestus:", viga)
