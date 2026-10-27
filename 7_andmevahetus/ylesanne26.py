from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re
URL = "https://example.com/"
try:
    with urlopen(URL, timeout=10) as vastus:
        html = vastus.read().decode("utf-8", errors="replace")
    print("Esimesed 300 tähemärki:")
    print(html[:300])
    print("Sisaldab <title> märgendit:", "<title>" in html.lower())
    print("<a  esinemiste arv:", html.lower().count("<a "))
    vaste = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    print("Lehe pealkiri:", re.sub(r"\s+", " ", vaste.group(1)).strip() if vaste else "Pealkirja ei leitud")
except (URLError, HTTPError, TimeoutError) as viga:
    print("Veebilehe lugemine ebaõnnestus:", viga)
