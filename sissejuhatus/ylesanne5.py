# Kontrollime iga teisenduse eraldi, et üks vigane näide ei peataks programmi.
examples = [
    ('int("123")', lambda: int("123")),
    ('int("12.3")', lambda: int("12.3")),
    ('float("12.3")', lambda: float("12.3")),
    ('float("tere")', lambda: float("tere")),
    ('str(25)', lambda: str(25)),
]
for label, convert in examples:
    try:
        print(label, "->", convert())
    except ValueError:
        print(label, "-> ValueError: tekst ei ole sobiv arv")
