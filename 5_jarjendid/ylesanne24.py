# Ülesanne 24. Sõnede analüüs
laused = [
    "Täna õpime Pythonit",
    "Järjendid on väga kasulikud",
    "Programmeerimine nõuab harjutamist",
    "Tartu on ilus linn",
]
kokku_a = 0
pikim_lause = laused[0]
for lause in laused:
    a_arv = lause.lower().count("a")
    kokku_a += a_arv
    print(f"{lause}: {len(lause)} tähemärki, a-tähti {a_arv}")
    if len(lause) > len(pikim_lause):
        pikim_lause = lause
print("Kõigis lausetes a-tähti kokku:", kokku_a)
print("Kõige pikem lause:", pikim_lause)
