# Ülesanne 28. Täishäälikute loendamine

def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöü"
    arv = 0
    for taht in tekst.lower():
        if taht in taishaalikud:
            arv += 1
    return arv

for tekst in ("Tere", "Õunapuu", ""):
    print(repr(tekst), "->", taishaalikuid(tekst))
