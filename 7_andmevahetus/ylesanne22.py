from urllib.request import urlopen
from urllib.error import URLError, HTTPError
URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    print(tekst, end="")
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
    print("Veebist lugemine ebaõnnestus:", viga)
