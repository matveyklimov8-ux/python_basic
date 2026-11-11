"""Ülesanne 45. Ostukorvi automaattestimine"""


from ostukorv import arvuta_summa, leia_kalleim, toodete_arv, rakenda_soodustus, eemalda_toode
korv = {"Leib": {"hind": 2.50, "kogus": 2}, "Piim": {"hind": 1.80, "kogus": 1}, "Juust": {"hind": 4.20, "kogus": 3}}
assert round(arvuta_summa(korv), 2) == 19.4
assert leia_kalleim(korv) == "Juust"
assert toodete_arv(korv) == 6
assert round(rakenda_soodustus(100, 10), 2) == 90
assert "Piim" not in eemalda_toode(korv, "Piim")
print("Ostukorvi põhikontrollid läbisid; detailsemad testid: test_ostukorv.py")
