"""Ülesanne 19. Esimene pytest testifail"""


# Eraldi fail test_ylesanne19.py lisab pytest-testid samale funktsioonile.
from testitavad_funktsioonid import suurem
assert suurem(3, 1)
assert not suurem(1, 3)
print("Näidistestid korras. pytesti kasutamiseks käivita pytest.")
