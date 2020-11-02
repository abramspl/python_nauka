import unittest
from populacja import miasto_funkcja

class TestMiastaDane(unittest.TestCase):
    """Test dla programu 'miasto_panstwo.py'."""

    def test_miasto_panstwo(self):
        """Czy dane 'Warszawa Polska' sa prawidlowo obslugiwane"""
        dane = miasto_funkcja('warszawa','polska')
        self.assertEqual(dane, 'Warszawa, Polska.')

    def test_miasto_populacja(self):
        dane = miasto_funkcja('warszawa','polska','45 000 000')
        self.assertEqual(dane, 'Warszawa, Polska - Populacja 45 000 000.')

if __name__ == '__main__':
    unittest.main()