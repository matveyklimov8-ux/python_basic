# Ülesanne 9. Muutujanimede kontrollimine
# keyword on Pythoni standardteegi moodul, mis tunneb keele reserveeritud sõnu.
# import teeb mooduli koodis kasutatavaks; keyword.iskeyword() kontrollib,
# kas nimi on näiteks if, for või class (selliseid nimesid muutujana kasutada ei saa).
import keyword

names = ["student_name", "2student", "student2", "student-name", "student name",
         "total_price", "class", "my_age"]

for name in names:
    valid = name.isidentifier() and not keyword.iskeyword(name)
    print(f"{name}: {'lubatud' if valid else 'ei ole lubatud'}")
