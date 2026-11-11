"""Puhtad funktsioonid automaattestimise harjutusteks."""
def suurem(a, b): return a > b
def on_paaris(arv): return arv % 2 == 0
def sona_pikkus(tekst): return len(tekst)
def celsius_fahrenheit(c): return c * 9 / 5 + 32
def hinne(punktid):
    if not 0 <= punktid <= 100: return None
    if punktid >= 90: return 5
    if punktid >= 75: return 4
    if punktid >= 50: return 3
    if punktid >= 20: return 2
    return 1
def palindroom(tekst):
    cleaned = "".join(c.casefold() for c in tekst if c.isalnum())
    return cleaned == cleaned[::-1]
def on_kolmnurk(a, b, c): return a > 0 and b > 0 and c > 0 and a+b>c and a+c>b and b+c>a
def soodushind(hind, protsent=10):
    if hind < 0 or not 0 <= protsent <= 100: raise ValueError("Vigane hind või allahindlus")
    return round(hind * (1 - protsent/100), 2)
def eemalda_taht(tekst, taht): return tekst.replace(taht, "")
def ostukorvi_summa(ostukorv): return round(sum(hind * kogus for hind, kogus in ostukorv.values()), 2)
def unikaalsed(jarjend):
    tulemus=[]
    for x in jarjend:
        if x not in tulemus: tulemus.append(x)
    return tulemus
def sona_sagedus(tekst):
    sagedus={}
    for sona in tekst.casefold().split(): sagedus[sona]=sagedus.get(sona,0)+1
    return sagedus
def parooli_tugevus(parool):
    tingimused = [len(parool)>=8, any(c.isupper() for c in parool), any(c.islower() for c in parool), any(c.isdigit() for c in parool), any(not c.isalnum() and not c.isspace() for c in parool)]
    return sum(tingimused)
def transpordikulu(summa, tasuta_alates=50, kulu=4.99):
    if summa < 0: raise ValueError("Summa ei tohi olla negatiivne")
    return 0.0 if summa >= tasuta_alates else round(kulu, 2)
def kalkulaator(a, b, tehe):
    if tehe == "+": return a+b
    if tehe == "-": return a-b
    if tehe == "*": return a*b
    if tehe == "/":
        if b == 0: raise ZeroDivisionError("Nulliga jagamine")
        return a/b
    raise ValueError("Tundmatu tehe")
