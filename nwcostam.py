# plik testy.py
import unittest
from funkcje import dodaj

class TestFunkcji(unittest.TestCase):

    def test_dodaj(self):
        self.assertEqual(dodaj(2, 3), 5)
        self.assertEqual(dodaj(-1, 1), 0)
        self.assertEqual(dodaj(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

