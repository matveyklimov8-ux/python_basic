"""Ülesanne 25. Suurima väärtuse leidmine"""


def suurim(arvud):
    if not arvud: return None
    parim = arvud[0]
    for arv in arvud[1:]:
        if arv > parim: parim = arv
    return parim
assert suurim([-5,-2,-10]) == -2
assert suurim([]) is None
