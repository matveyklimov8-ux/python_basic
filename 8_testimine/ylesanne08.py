"""Ülesanne 8. Hinde määramine"""


from testitavad_funktsioonid import hinne
for p, h in [(100,5),(90,5),(89,4),(75,4),(74,3),(50,3),(49,2),(20,2),(19,1),(0,1),(-1,None),(101,None)]: assert hinne(p) == h
