"""Ülesanne 31. Esimene unittest.TestCase"""


import unittest
from testitavad_funktsioonid import suurem
class TestSuurem(unittest.TestCase):
    def test_suurem(self): self.assertTrue(suurem(5, 2))
    def test_mitte_suurem(self): self.assertFalse(suurem(2, 5))
if __name__ == "__main__": unittest.main()
