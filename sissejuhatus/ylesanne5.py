# Ülesanne 5. Teisendused ja vigase sisendi käsitlemine
# lambda loob väikese nimeta funktsiooni. Siin hoiab iga lambda ühe teisenduse
# eraldi: kui seda kutsutakse, tagastab see vastava teisenduse tulemuse.
examples = [
    ('int("123")', lambda: int("123")),
    ('int("12.3")', lambda: int("12.3")),
    ('float("12.3")', lambda: float("12.3")),
    ('float("tere")', lambda: float("tere")),
    ('str(25)', lambda: str(25)),
]

for label, convert in examples:
    try:
        # convert() käivitab hetkel valitud lambda-funktsiooni.
        print(label, "->", convert())
    except ValueError:
        # int() või float() tekitab ValueError-i, kui tekst ei sobi arvuks.
        # except püüab vea kinni, et järgmisi näiteid saaks edasi töödelda.
        print(label, "-> ValueError: tekst ei ole sobiv arv")
