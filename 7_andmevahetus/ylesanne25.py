from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re
URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
otsitav = input("Sisesta otsitav sõna: ").strip().casefold()
if not otsitav:
    print("Otsitav sõna ei tohi olla tühi.")
else:
    try:
        with urlopen(URL, timeout=10) as vastus:
            tekst = vastus.read().decode("utf-8")
        sonad = [sona.casefold() for sona in re.findall(r"[^\W\d_]+", tekst, flags=re.UNICODE)]
        print(f"Sõna '{otsitav}' esineb tekstis {sonad.count(otsitav)} korda.")
    except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
        print("Veebiteksti ei õnnestunud lugeda:", viga)
