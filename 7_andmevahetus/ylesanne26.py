# Ülesanne 26. Veebilehe HTML-koodi uurimine
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

URL = "https://example.com/"
try:
    with urlopen(URL, timeout=10) as vastus:
        html = vastus.read().decode("utf-8", errors="replace")

    # Ülesandes nõutud tekstimeetodid: lõikamine, find() ja count().
    html_lower = html.lower()
    print("Esimesed 300 tähemärki:")
    print(html[:300])

    title_position = html_lower.find("<title")
    print("Sisaldab <title> märgendit:", title_position != -1)
    print("<a  esinemiste arv:", html_lower.count("<a "))

    # Leiame avava märgendi lõpumärgi ja seejärel sulgeva </title> märgendi.
    title = "Pealkirja ei leitud"
    if title_position != -1:
        title_start = html_lower.find(">", title_position)
        title_end = html_lower.find("</title>", title_start + 1)
        if title_start != -1 and title_end != -1:
            title = " ".join(html[title_start + 1:title_end].split())
    print("Lehe pealkiri:", title)
except (URLError, HTTPError, TimeoutError, UnicodeDecodeError) as viga:
    print("Veebilehe lugemine ebaõnnestus:", viga)
