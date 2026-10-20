# 6. Funktsioonid — lahendused

Iga fail `ylesanneNN.py` sisaldab ühe Moodle'i ülesande lahendust. Graafikaga ülesanded 40–45 kasutavad Tkinteri akent ning vajavad graafilist töölauaseanssi.

Kohustuslik kontrollülesanne asub failis `opilaste_hinnete_haldussusteem.py`.

## Käivitamine
Avage projekt VS Code'is ja valige soovitud fail. Käivitage terminalis näiteks:

```bash
python3 6_funktsioonid/ylesanne13.py
python3 6_funktsioonid/opilaste_hinnete_haldussusteem.py
```

Kontrollige kogu teema süntaksit:

```bash
python3 -m compileall -q 6_funktsioonid
```

## Peamised ideed
- `def` määrab funktsiooni; `nimi(...)` kutsub selle välja.
- Parameetrid võtavad funktsioonile antud väärtused vastu.
- `return` tagastab väärtuse; `print()` kuvab väärtuse ekraanile.
- Lokaalne muutuja eksisteerib ainult funktsiooni sees.
- Graafikafunktsioonid saavad Canvas-objekti ja koordinaadid argumentidena.
- Kontrollülesanne kasutab eraldi funktsioone, kahte seotud järjendit, sisendi valideerimist ja menüüd.
