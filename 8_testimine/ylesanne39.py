"""Ülesanne 39. Koodi ümberkorraldamine testide abil"""


# Arvutus eraldatakse kasutajasisendist: nii saab seda kutsuda ilma terminali sisendita.
def brutohind(hind, maks): return round(hind * (1 + maks), 2)
assert brutohind(100, 0.24) == 124
