import unittest
from miasto_panstwo import miasto_funkcja

class TestMiastaDane(unittest.TestCase):
    """Test dla programu 'miasto_panstwo.py'."""

    def test_miasto_panstwo(self):
        """Czy dane 'Warszawa Polska' sa prawidlowo obslugiwane"""
        dane = miasto_funkcja('warszawa','polska')
        self.assertEqual(dane, 'Warszawa, Polska.')

if __name__ == '__main__':
    unittest.main()