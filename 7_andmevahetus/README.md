# 7. Andmevahetus — lahendused

Pakk sisaldab 38 tavalist ülesannet, kohustuslikku kontrollülesannet ning näidisandmeid.

## Failid
- `ylesanne01.py` kuni `ylesanne38.py` — Moodle'i ülesanded nende järjekorras.
- `opilaste_tulemuste_tootlemine.py` — kohustuslik kontrollülesanne.
- `.txt`-failid — näidisandmed, mida kasutavad programmid.

## Käivitamine
Ava konkreetne `.py`-fail VS Code'is ja vajuta Run Python File. Koodi failiteed põhinevad `Path(__file__)` abil skripti asukohal, seega käivitamine töötab ka siis, kui terminali praegune kataloog on mujal.

Enne kontrolltöö programmi käivitamist veendu, et `tulemused.txt` asub samas kaustas.

## Veebiharjutused
Ülesanded 22–27 ja 37 vajavad internetiühendust. Need kasutavad `urllib.request`-i ning käsitlevad tavalisi ühendusvigu. Veebiteksti sisu võib muutuda; kontrolli õpetaja antud URL-i, kui näidisallikas ei tööta.

## Märkus ülesande 10 kohta
Moodle'i näidistekstis on antud lausete järgi 13 sõna, kuigi näidisväljund ütleb 15. Programm loendab tegelikud sõnad failist ega kirjuta vastust käsitsi sisse.

## Kontroll
Kogu teema Python-failid kompileeruvad. Tkinteri ülesannet 38 tuleb käivitada graafilises töölauakeskkonnas, et akent näha.

## Märkus kohustusliku kontrolltöö näidisväljundi kohta

Moodle näitab klassi keskmiseks 68.96, kuid esitatud kaheksa õpilase punktide aritmeetiline keskmine on 72.42 (1738 punkti / 24 tulemust). Ülesande üksikõpilaste keskmised kinnitavad samuti 72.42. Programm arvutab tulemuse lähteandmetest, mitte ei kirjuta näidisväärtust käsitsi sisse; 68.96 näib Moodle näites olevat arvutusviga.
