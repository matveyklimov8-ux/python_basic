"""Ülesanne 35. Funktsioon testidest lähtudes"""


# Funktsiooni piirjuhud tuleb tuletada testide nõuetest.
def jaga(a, b):
    if b == 0: return None
    return a / b
assert jaga(10, 2) == 5
assert jaga(1, 0) is None
