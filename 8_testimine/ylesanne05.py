"""Ülesanne 5. Vigase funktsiooni avastamine"""


# Vigane variant oleks: def suurem(a,b): return a < b
from testitavad_funktsioonid import suurem
assert suurem(10, 1) is True
assert suurem(1, 10) is False
print("Testid aitavad märgata valepidi võrdlust.")
