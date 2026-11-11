# 8. Testimine

`assert`, pytest, unittest, piirväärtused, erindid ja ostukorvi testid.

## Ülesanded

- [`ylesanne01.py`](ylesanne01.py) — Esimene automaattest
- [`ylesanne02.py`](ylesanne02.py) — Kahe arvu võrdlemine
- [`ylesanne03.py`](ylesanne03.py) — Paaris- ja paaritud arvud
- [`ylesanne04.py`](ylesanne04.py) — Sõne pikkus
- [`ylesanne05.py`](ylesanne05.py) — Vigase funktsiooni avastamine
- [`ylesanne06.py`](ylesanne06.py) — Testide parandamine
- [`ylesanne07.py`](ylesanne07.py) — Temperatuuri teisendamine
- [`ylesanne08.py`](ylesanne08.py) — Hinde määramine
- [`ylesanne09.py`](ylesanne09.py) — Palindroomi kontrollimine
- [`ylesanne10.py`](ylesanne10.py) — Kolmnurga kontrollimine
- [`ylesanne11.py`](ylesanne11.py) — Soodustuse arvutamine
- [`ylesanne12.py`](ylesanne12.py) — Liiga vähesed testid
- [`ylesanne13.py`](ylesanne13.py) — print() asendamine return-iga
- [`ylesanne14.py`](ylesanne14.py) — Tähtede eemaldamine sõnest
- [`ylesanne15.py`](ylesanne15.py) — input() eraldamine arvutusest
- [`ylesanne16.py`](ylesanne16.py) — Ostukorvi kogusumma
- [`ylesanne17.py`](ylesanne17.py) — Globaalmuutujast sõltuv funktsioon
- [`ylesanne18.py`](ylesanne18.py) — Testitavuse analüüs
- [`ylesanne19.py`](ylesanne19.py) — Esimene pytest testifail
- [`ylesanne20.py`](ylesanne20.py) — Testide veateadete lugemine
- [`ylesanne21.py`](ylesanne21.py) — Parameetriseeritud testid
- [`ylesanne22.py`](ylesanne22.py) — Erindite testimine
- [`ylesanne23.py`](ylesanne23.py) — Testide rühmitamine
- [`ylesanne24.py`](ylesanne24.py) — Vigase koodi parandamine testide põhjal
- [`ylesanne25.py`](ylesanne25.py) — Suurima väärtuse leidmine
- [`ylesanne26.py`](ylesanne26.py) — Korduvate elementide eemaldamine
- [`ylesanne27.py`](ylesanne27.py) — Sõnade sageduse arvutamine
- [`ylesanne28.py`](ylesanne28.py) — Õpilaste hinnete analüüs
- [`ylesanne29.py`](ylesanne29.py) — Hulgatehete kontrollimine
- [`ylesanne30.py`](ylesanne30.py) — Andmestruktuuri muutmise avastamine
- [`ylesanne31.py`](ylesanne31.py) — Esimene unittest.TestCase
- [`ylesanne32.py`](ylesanne32.py) — Erinevad kontrollimeetodid
- [`ylesanne33.py`](ylesanne33.py) — Erindite kontrollimine
- [`ylesanne34.py`](ylesanne34.py) — pytest ja unittest võrdlemine
- [`ylesanne35.py`](ylesanne35.py) — Funktsioon testidest lähtudes
- [`ylesanne36.py`](ylesanne36.py) — Parooli tugevuse kontrollimine
- [`ylesanne37.py`](ylesanne37.py) — Pangakonto saldo
- [`ylesanne38.py`](ylesanne38.py) — Tellimuse transpordikulu
- [`ylesanne39.py`](ylesanne39.py) — Koodi ümberkorraldamine testide abil
- [`ylesanne40.py`](ylesanne40.py) — Kalkulaatori testimine
- [`ylesanne41.py`](ylesanne41.py) — Tekstitöötluse tööriist
- [`ylesanne42.py`](ylesanne42.py) — Õpilaste tulemuste analüüs
- [`ylesanne43.py`](ylesanne43.py) — Vigadega raamatukogusüsteem
- [`ylesanne44.py`](ylesanne44.py) — Isikliku projekti automaattestimine
- [`ylesanne45.py`](ylesanne45.py) — Ostukorvi automaattestimine

## Kohustuslikud tööd ja abifailid

- `ostukorv.py`
- `raamatukogu.py`
- `test_ostukorv.py`
- `test_raamatukogu.py`
- `testitavad_funktsioonid.py`

## Käivitamine

Ava VS Code terminal selles kaustas ja käivita näiteks:

```bash
python3 ylesanne01.py
```

Failipõhised ülesanded kasutavad sama kausta näidisandmeid. Graafilised ülesanded vajavad graafilist töölaua seanssi.


## Kohustuslik ülesanne 45 — Ostukorvi automaattestimine

Moodulis `ostukorv.py` on viis nõutud funktsiooni: `arvuta_summa`, `leia_kalleim`, `toodete_arv`, `rakenda_soodustus` ja `eemalda_toode`. Testid asuvad failis `test_ostukorv.py` ning kontrollivad tavalisi sisendeid, tühja ostukorvi, viiki kõige kallima toote leidmisel, soodustuse piire, vigaseid hindu ja koguseid ning algse ostukorvi säilimist. Testides kasutatakse ka `@pytest.mark.parametrize`-dekoraatorit ja `pytest.raises`-konstruktsiooni.

### Testide käivitamine

Ava terminal just selles kaustas ja käivita:

```bash
python -m pip install pytest
python -m pytest -q test_ostukorv.py
```

Kontrollimise ajal käsitleti eraldi olukorda, kus mitmel tootel on sama kõrgeim ühikuhind: funktsioon peab valima nime tähestikulises järjekorras. Samuti kontrollivad testid, et `eemalda_toode()` ei muudaks algset ostukorvi. Need piirjuhtumid aitavad vältida juhuslikku tulemuse sõltumist andmete järjekorrast või algandmete muutmist.

Viimase kontrolli tulemus pärast täiendusi: **27 testi läbisid** (`test_ostukorv.py`). Koos `test_raamatukogu.py` testidega läbis kogu selle kausta valitud testikomplekt **42 testi**.
