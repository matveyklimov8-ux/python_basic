"""Ülesanne 32. Erinevad kontrollimeetodid"""


import unittest
class TestMeetodid(unittest.TestCase):
    def test_meetodid(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2, 3)
        self.assertIn("Py", "Python")
        self.assertTrue(3 > 0)
        self.assertIsNone(None)
if __name__ == "__main__": unittest.main()
