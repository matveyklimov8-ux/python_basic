"""Ülesanne 21. Parameetriseeritud testid"""


from testitavad_funktsioonid import hinne
juhtumid = [(0,1),(19,1),(20,2),(49,2),(50,3),(74,3),(75,4),(89,4),(90,5),(100,5)]
for punktid, ootus in juhtumid: assert hinne(punktid) == ootus
print("Kõik parameetriseeritud juhtumid läbisid.")
