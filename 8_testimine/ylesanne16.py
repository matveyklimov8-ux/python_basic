"""Ülesanne 16. Ostukorvi kogusumma"""


from testitavad_funktsioonid import ostukorvi_summa
assert ostukorvi_summa({"Leib": (2.5,2), "Piim": (1.8,1)}) == 6.8
assert ostukorvi_summa({}) == 0
