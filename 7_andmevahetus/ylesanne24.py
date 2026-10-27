from urllib.request import urlopen
from urllib.error import URLError, HTTPError
URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    read = tekst.splitlines()
    sonad = tekst.split()
    print("Veebiteksti statistika")
    print("----------------------")
    print("Ridu:", len(read))
    print("Sõnu:", len(sonad))
    print("Tähemärke:", len(tekst))
    print("Tühje ridu:", sum(1 for rida in read if not rida.strip()))
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
    print("Veebiteksti ei õnnestunud lugeda:", viga)
