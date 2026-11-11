"""Ülesanne 33. Erindite kontrollimine"""


import unittest
from testitavad_funktsioonid import kalkulaator, soodushind
class TestErindid(unittest.TestCase):
    def test_nulliga_jagamine(self):
        with self.assertRaises(ZeroDivisionError): kalkulaator(1, 0, "/")
    def test_vigane_soodustus(self):
        with self.assertRaises(ValueError): soodushind(10, 120)
if __name__ == "__main__": unittest.main()
