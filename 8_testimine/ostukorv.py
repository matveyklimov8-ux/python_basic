"""Funktsioonid ostukorvi hinnastamiseks; sobib pytestiga testimiseks."""
def _valideeri(ostukorv):
    for nimi, info in ostukorv.items():
        if not isinstance(info, dict) or "hind" not in info or "kogus" not in info:
            raise ValueError(f"Toote {nimi!r} kirje peab sisaldama hinda ja kogust.")
        hind = info["hind"]; kogus = info["kogus"]
        if not isinstance(hind, (int, float)) or isinstance(hind, bool): raise ValueError("Hind peab olema arvuline.")
        if hind < 0: raise ValueError("Hind ei tohi olla negatiivne.")
        if not isinstance(kogus, int) or isinstance(kogus, bool): raise ValueError("Kogus peab olema täisarv.")
        if kogus < 0: raise ValueError("Kogus ei tohi olla negatiivne.")
def arvuta_summa(ostukorv):
    _valideeri(ostukorv)
    return round(sum(info["hind"] * info["kogus"] for info in ostukorv.values()), 2)
def leia_kalleim(ostukorv):
    _valideeri(ostukorv)
    if not ostukorv: return None
    return sorted(ostukorv, key=lambda nimi: (-ostukorv[nimi]["hind"], nimi.casefold()))[0]
def toodete_arv(ostukorv):
    _valideeri(ostukorv)
    return sum(info["kogus"] for info in ostukorv.values())
def rakenda_soodustus(summa, protsent):
    if (not isinstance(summa, (int, float)) or isinstance(summa, bool)
            or summa < 0):
        raise ValueError("Summa peab olema mittenegatiivne arv.")
    if (not isinstance(protsent, (int, float)) or isinstance(protsent, bool)
            or not 0 <= protsent <= 100):
        raise ValueError("Soodustus peab olema vahemikus 0–100%.")
    return round(summa * (1 - protsent / 100), 2)
def eemalda_toode(ostukorv, nimi):
    _valideeri(ostukorv)
    uus = {toode: info.copy() for toode, info in ostukorv.items() if toode != nimi}
    return uus
