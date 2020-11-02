import unittest
from pracownik import Pracownik

class TestPracownik(unittest.TestCase):

    def test_podwyzka_domyslnie(self):
        egzemplarz = Pracownik('imie','nazwisko',1000)
        egzemplarz.dac_podwyzke()
        self.assertEqual(6000,egzemplarz.wynagrodzenie_roczne)

    def test_podwyzka_kwota(self):
        egzemplarz = Pracownik('imie','nazwisko',1000)
        egzemplarz.dac_podwyzke(2000)
        self.assertEqual(3000,egzemplarz.wynagrodzenie_roczne)

if __name__ == '__main__':
    unittest.main()