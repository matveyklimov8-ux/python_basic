"""Ülesanne 12. Liiga vähesed testid"""


from testitavad_funktsioonid import hinne
# Ära testi ainult keskmist juhtu; lisa piirid mõlemal pool iga lävendit.
for p, expected in [(89,4),(90,5),(74,3),(75,4),(49,2),(50,3)]: assert hinne(p) == expected
