"""Ülesanne 20. Testide veateadete lugemine"""


# Käivita üks vigane assert ja vaata, millist tegelikku ja oodatud väärtust näidatakse.
from testitavad_funktsioonid import hinne
tegelik = hinne(90); oodatud = 5
assert tegelik == oodatud, f"Oodati {oodatud}, saadi {tegelik}"
