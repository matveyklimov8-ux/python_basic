"""Ülesanne 10. Kolmnurga kontrollimine"""


from testitavad_funktsioonid import on_kolmnurk
assert on_kolmnurk(3,4,5)
assert not on_kolmnurk(1,2,10)
assert not on_kolmnurk(0,2,2)
