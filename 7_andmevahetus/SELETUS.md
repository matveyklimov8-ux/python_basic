# 7. Andmevahetus — lühike seletus

- **`open(..., encoding="utf-8")`** avab teksti UTF-8 kodeeringus.
- **`read()`** loeb kogu faili ühe stringina; **`for rida in fail`** loeb faili rea kaupa.
- **`strip()`** eemaldab rea algusest ja lõpust tühikud ning reavahetuse.
- **`int()` / `float()`** muudavad failist saadud teksti arvuks.
- **`with open(...)`** sulgeb faili automaatselt ka siis, kui tekib viga.
- **`"w"`** kirjutab faili algusest ja asendab vana sisu; **`"a"`** lisab faili lõppu.
- **`try/except FileNotFoundError`** võimaldab anda arusaadava teate, kui faili pole.
- **`urlopen()`** avab veebiaadressi; `read()` annab baidid ja `decode("utf-8")` muudab need tekstiks.
- **`Path(__file__).with_name(...)`** leiab andmefaili samast kaustast, kus asub Python-skript.
- Kohustuslikus töös loetakse iga õpilase kolm tulemust, leitakse keskmine ning selle järgi hinne; kõik arvutatud tulemused kirjutatakse `aruanne.txt` faili.

**Oluline märkus:** ülesande näidis ütleb, et klassi keskmine on 68.96, kuid failis toodud 24 tulemuse summa on 1738 ja 1738 / 24 = 72.4167, seega õige kahe komakohaga keskmine on 72.42. Kood kasutab andmetest arvutatud tulemust.
