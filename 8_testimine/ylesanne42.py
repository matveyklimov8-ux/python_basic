"""Ülesanne 42. Õpilaste tulemuste analüüs"""


from testitavad_funktsioonid import hinne
punktid = [78, 45, 92, 67, 34, 100, 56, 81]
assert sum(punktid)/len(punktid) == 69.125
assert hinne(100) == 5
assert sum(p >= 50 for p in punktid) == 6
