"""Ülesanne 36. Parooli tugevuse kontrollimine"""


from testitavad_funktsioonid import parooli_tugevus
assert parooli_tugevus("abc") == 2
assert parooli_tugevus("Tugev123!") == 5
