# Parandused õpetaja tagasiside põhjal

See fail võtab kokku õpetaja nimetatud täiendused teemades 1–7. Parandatud lähtekood on vastavate teemade kaustades.

## 1. Sissejuhatus
- `ylesanne5.py`: lisatud selgitused `lambda`-funktsiooni ning `try/except ValueError` kohta.
- `ylesanne9.py`: dünaamiline `__import__()` asendatud tavapärase `import keyword` kasutamisega ja lisatud selgitus.

## 3. Tsüklid
- Ülesanded 1, 2, 7 ja 9: lisatud väljundi prognoosid ning muutujate muutumise selgitused.
- Ülesanded 29 ja 31: lisatud juhuslike katsete oodatava keskmise ja korduvkäivituste erinevuse selgitused.
- Ülesanded 36–38: lisatud selgitused piiritingimuse ja loenduri suurendamise kohta. Selles eksporditud lahenduste komplektis olid alles ainult parandatud lühikesed tsüklid, mitte algsed vigased lähteprogrammid; seetõttu kirjeldavad kommentaarid kontrollitavaid piiri- ja lõpetamistingimusi, mitte õpetajale esitamata algse vea oletatavat täpset kuju.

## 4. Sõned
- Ülesanne 7: prognoosid lisatud kommentaarina.
- Ülesanne 21: menüü küsib enne tegevuse valiku ja seejärel töödeldava teksti.
- Ülesanne 32: viimase koordinaadi sildid paigutatakse lõuendi sisse.
- Ülesanne 36: ringide paigutus arvutatakse lõuendi mõõtmete järgi; lubatud maksimumi ületamisel näidatakse selget viga.
- Ülesanne 39: teksti värv valitakse tausta heleduse järgi.

## 5. Järjendid
- Ülesannete 03 ja 08 prognoosid on eraldi failis `ENNUSTUSED.md`.
- Ülesande 33 sagedusdiagrammi juurde lisatakse ka arvuline sagedus.
- Ülesandes 37 kasutatakse sõna `Python` leidmiseks `lower()`-meetodit, mitte regulaaravaldist.

## 6. Funktsioonid
- Ülesanne 18: mõlemad funktsioonid tagastavad väärtuse ja nende tulemusi kasutatakse uutes arvutustes.
- Ülesanne 34: selgitatud, miks lokaalse muutuja kasutamine väljaspool funktsiooni tekitab `NameError`-i.
- Ülesanne 49: `check_password()` tagastab ainult täidetud tingimuste arvu (0–5); `count_failed_conditions()` loendab täitmata tingimusi.
- Märkus sõnade `student` ja `students` kohta: esitatud lahenduste kaustas ei olnud vastavat ingliskeelset statistikatesti ega selliseid väljundsõnu, mida oleks saanud täpselt parandada. Olemasoleva õpilaste statistika väljund kasutab eesti termineid (`õpilast`, `õpilast` kontekstis). Kui õpetaja pidas silmas mõnda eraldi testi faili, pole seda selles lähtekomplektis.

## 7. Andmevahetus
- Ülesanne 14: `tekst.txt` sisaldab nüüd vähemalt 10 sisulist rida.
- Ülesanded 25–27: lisatud selgitused otsingule ja failitöötlusele; 26 kasutab nõutud `find()`, `count()` ja lõikamist; 27 avab salvestatud faili uuesti.
- Ülesanne 29: aruandefail sisaldab iga toote müügitulu, kogu müügitulu ja suurima tuluga toodet.
- Ülesanne 33: tulemused salvestatakse `comparison.txt` faili.

## Täiendav teema 8 — Testimine
Kohustuslik ülesanne 45 (`Ostukorvi automaattestimine`) on lisatud eraldi `8_testimine` kausta. Seal on `ostukorv.py`, `test_ostukorv.py` ja README koos käivituskäsu ning testitulemuste kirjeldustega.
