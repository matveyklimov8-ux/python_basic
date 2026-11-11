"""Ülesanne 34. pytest ja unittest võrdlemine"""


# pytest: lihtsad assert-käsud ja parameetriseerimine. unittest: TestCase klass ja meetodid.
from testitavad_funktsioonid import suurem
assert suurem(3, 2)
import unittest
class TestNäide(unittest.TestCase):
    def test_võrdlus(self): self.assertTrue(suurem(3,2))
if __name__ == "__main__": unittest.main()
