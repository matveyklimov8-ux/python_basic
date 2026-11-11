# Ülesanne 25. Terve sõna otsimine veebitekstist
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re

URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
otsitav = input("Sisesta otsitav sõna: ").strip()

if not otsitav:
    print("Otsitav sõna ei tohi olla tühi.")
else:
    try:
        with urlopen(URL, timeout=10) as vastus:
            tekst = vastus.read().decode("utf-8")

        # casefold() muudab teksti ja otsitava sõna võrdlemiseks ühtsesse registrisse.
        # Piirid (?<!\w) ja (?!\w) välistavad sõnaosad: näiteks 'test' ei sobi 'testing'.
        otsingutekst = tekst.casefold()
        muster = r"(?<!\w)" + re.escape(otsitav.casefold()) + r"(?!\w)"
        vasteid = re.findall(muster, otsingutekst, flags=re.UNICODE)
        print(f"Terve sõna '{otsitav}' esineb tekstis {len(vasteid)} korda.")
    except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
        print("Veebiteksti ei õnnestunud lugeda:", viga)
