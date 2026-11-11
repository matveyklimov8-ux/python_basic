"""Ülesanne 44. Isikliku projekti automaattestimine"""


# Näidis: funktsioonide põhifunktsionaalsus kontrollitakse ilma input/print sõltuvuseta.
from testitavad_funktsioonid import kalkulaator, palindroom, soodushind
assert kalkulaator(7, 5, "+") == 12
assert palindroom("Radar")
assert soodushind(50, 20) == 40
print("Näidistestid korras; täiendavad testid asuvad testide failis.")
