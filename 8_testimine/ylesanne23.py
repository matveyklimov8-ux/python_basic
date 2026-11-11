"""Ülesanne 23. Testide rühmitamine"""


# pytestis saab rühmitada klassidesse või märkidega; siin on näide lihtsast rühmitusest.
from testitavad_funktsioonid import on_paaris, sona_pikkus
class TestArvud:
    def test_paaris(self): assert on_paaris(8)
class TestSoned:
    def test_pikkus(self): assert sona_pikkus("abc") == 3
for test in (TestArvud().test_paaris, TestSoned().test_pikkus): test()
print("Rühmitatud näited läbisid.")
