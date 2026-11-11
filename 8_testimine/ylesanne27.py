"""Ülesanne 27. Sõnade sageduse arvutamine"""


from testitavad_funktsioonid import sona_sagedus
assert sona_sagedus("Python python Git") == {"python": 2, "git": 1}
