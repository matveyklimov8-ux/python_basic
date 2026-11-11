# Python: parandused tagasiside põhjal + lisateema 8

See komplekt sisaldab kahte eraldi osa:

- `python_basic/` — õpetaja tagasiside põhjal parandatud sinu olemasolevate teemade 1–7 lahendused.
- `8_testimine/` — lisateema 8 ülesannete kogumik ning kohustuslik ülesanne 45 `Ostukorvi automaattestimine` koos testide ja README-ga.

## Käivitamine

Põhiteemade süntaksikontroll:

```bash
cd python_basic
python3 -m compileall -q sissejuhatus 2_tingimuslaused 3_tsuklid 4_soned 5_jarjendid 6_funktsioonid 7_andmevahetus
```

Lisateema 8 automaattestid:

```bash
cd 8_testimine
python3 -m pip install pytest
python3 -m pytest -q test_ostukorv.py
```

## Olulised märkused

- Tkinteri ülesandeid (`4_soned`) tuleb visuaalselt kontrollida graafilises töölauaseansis. Siin kontrolliti nende süntaksit, mitte akende välimust.
- Veebiülesanded (`7_andmevahetus` 25–27) vajavad töötavat internetiühendust. Nende väliste päringute tulemust ei ole selles kontrollis kinnitatud.
- Tsüklite ülesannete 36–38 algseid vigaseid lähteprogramme ei olnud olemasolevas ekspordis. Neile lisati selgitused piirtingimuste ja loenduri suurendamise kohta, kuid algse vea täpset kuju pole oletatud.
- Õpetaja mainitud `student/students` sõnastuse näidet ei olnud esitatud failides leida; see on dokumenteeritud failis `python_basic/TAGASISIDE_PARANDUSED.md`.

Paranduste täielik loend: `python_basic/TAGASISIDE_PARANDUSED.md`.
Vene keelne juhis: `python_basic/ИСПРАВЛЕНИЯ_ПО-РУССКИ.md`.
