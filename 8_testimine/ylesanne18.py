"""Ülesanne 18. Testitavuse analüüs"""


# Funktsioon on lihtsamini testitav, kui ta ei küsi ise input() ega väljasta print().
def kasvanud(vanus): return vanus + 1
assert kasvanud(17) == 18
