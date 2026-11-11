"""Ülesanne 43. Vigadega raamatukogusüsteem"""


# Parandatud raamatukogufunktsioonid on moodulis raamatukogu.py; testid test_raamatukogu.py.
from raamatukogu import Raamatukogu
r = Raamatukogu({"Python": 3, "Java": 2, "Linux": 1})
assert r.laenuta("Python")
assert r.saadavus("Python") == 2
assert not r.laenuta("Puuduv")
assert r.tagasta("Python")
assert r.saadavus("Python") == 3
