"""Ülesanne 2. Kahe arvu võrdlemine"""


from testitavad_funktsioonid import suurem
for a, b, ootus in [(5,3,True),(3,5,False),(4,4,False)]:
    assert suurem(a,b) == ootus
print("Võrdlustestid läbisid.")
