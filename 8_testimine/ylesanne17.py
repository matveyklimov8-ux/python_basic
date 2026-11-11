"""Ülesanne 17. Globaalmuutujast sõltuv funktsioon"""


# Parem: edasta hind parameetrina, ära sõltu muudetavast globaalsest väärtusest.
def koos_maksuga(hind, maar=0.24): return round(hind * (1+maar), 2)
assert koos_maksuga(100, 0.2) == 120
