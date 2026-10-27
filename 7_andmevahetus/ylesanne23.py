from urllib.request import urlopen
from urllib.error import URLError, HTTPError
URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
try:
    with urlopen(URL, timeout=10) as vastus:
        read = vastus.read().decode("utf-8").splitlines()
    for i, rida in enumerate(read[:10], start=1):
        print(f"{i}: {rida}")
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
    print("Veebiteksti ei õnnestunud lugeda:", viga)
