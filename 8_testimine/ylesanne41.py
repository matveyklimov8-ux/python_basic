"""Ülesanne 41. Tekstitöötluse tööriist"""


from testitavad_funktsioonid import eemalda_taht, sona_sagedus
assert eemalda_taht("banana", "a") == "bnn"
assert sona_sagedus("A a b") == {"a": 2, "b": 1}
