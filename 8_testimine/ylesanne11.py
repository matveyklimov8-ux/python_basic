"""Ülesanne 11. Soodustuse arvutamine"""


from testitavad_funktsioonid import soodushind
assert soodushind(100, 10) == 90
assert soodushind(100, 0) == 100
assert soodushind(100, 100) == 0
