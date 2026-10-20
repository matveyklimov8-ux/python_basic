# Ülesanne 47. Õpilaste tulemuste analüüs

def keskmine(punktid):
    if not punktid:
        return None
    summa = 0
    for punkt in punktid:
        summa += punkt
    return summa / len(punktid)

def parim_tulemus(punktid):
    if not punktid:
        return None
    parim = punktid[0]
    for punkt in punktid[1:]:
        if punkt > parim:
            parim = punkt
    return parim

def norgim_tulemus(punktid):
    if not punktid:
        return None
    norgim = punktid[0]
    for punkt in punktid[1:]:
        if punkt < norgim:
            norgim = punkt
    return norgim

def edukate_arv(punktid, piir=50):
    kogus = 0
    for punkt in punktid:
        if punkt >= piir:
            kogus += 1
    return kogus

punktid = [78, 45, 92, 67, 34, 100, 56, 81]
print("Keskmine:", f"{keskmine(punktid):.2f}")
print("Parim tulemus:", parim_tulemus(punktid))
print("Nõrgim tulemus:", norgim_tulemus(punktid))
print("Vähemalt 50 punkti:", edukate_arv(punktid))
