from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
kaust = Path(__file__).resolve().parent
url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
allikas = "veebitekst_arhiiv.txt"
veebifail = kaust / allikas
try:
    with urlopen(url, timeout=10) as vastus:
        tekst = vastus.read().decode("utf-8")
    veebifail.write_text(tekst, encoding="utf-8")
    print("Uus veebitekst salvestati kohalikku faili.")
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError, OSError) as viga:
    print("Veebipäring ebaõnnestus:", viga)
    varufail = kaust / "veebitekst.txt"
    if varufail.exists():
        tekst = varufail.read_text(encoding="utf-8")
        print("Kasutan varem salvestatud veebiteksti.")
    elif veebifail.exists():
        tekst = veebifail.read_text(encoding="utf-8")
        print("Kasutan arhiivis olevat varasemat teksti.")
    else:
        tekst = ""
        print("Kohalikku varukoopiat pole saadaval.")
if tekst:
    read = tekst.splitlines(); sonad = tekst.split()
    aruanne = (f"Ridu: {len(read)}\nSõnu: {len(sonad)}\nTähemärke: {len(tekst)}\nTühje ridu: {sum(1 for r in read if not r.strip())}\n")
    (kaust / "veebiteksti_statistika.txt").write_text(aruanne, encoding="utf-8")
    print(aruanne, end="")
