"""Ülesanne 1. Esimene automaattest"""


from testitavad_funktsioonid import suurem
assert suurem(5, 3) is True
assert suurem(2, 7) is False
print("Esimesed testid läbisid.")
