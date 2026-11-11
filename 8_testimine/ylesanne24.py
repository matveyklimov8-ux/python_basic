"""Ülesanne 24. Vigase koodi parandamine testide põhjal"""


from testitavad_funktsioonid import on_kolmnurk
assert on_kolmnurk(3,4,5)
assert not on_kolmnurk(1,2,3)  # Võrdne summa ei anna kolmnurka.
assert not on_kolmnurk(-1,2,2)
