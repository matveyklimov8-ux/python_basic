"""Ülesanne 26. Korduvate elementide eemaldamine"""


from testitavad_funktsioonid import unikaalsed
assert unikaalsed([4,7,4,9,7]) == [4,7,9]
assert unikaalsed([]) == []
