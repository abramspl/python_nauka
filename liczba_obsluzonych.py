class Restauracja():
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.liczba_obsluzonych = 0

    def info(self):
        print(f'\nJest to restauracja o nazwie: {self.nazwa.title()}')
        print(f'Jej specjalizacja jest {self.rodzaj.upper()}')

    def godziny(self):
        print('\nGodziny funkcjonowania restauracji:')
        print('\t* PON - PIA (12-22)\n\t* SOB - NDZ (12-23)')

    def liczba_klientow(self):
        """Informacja o liczbie obsluzonych klietow"""
        print(f'\nRestauracja "{self.nazwa.upper()}" obsluzyła dzisiaj {self.liczba_obsluzonych} klietow!')

    def obsluzeni_klieci(self,liczba):
        """Zmiana wartosci domyslnej: liczba_obsluzonych"""
        self.liczba_obsluzonych = liczba

    def increment_liczby_obsluzonych(self,klieci):
        """Dodanie nowej wartosci do: liczba_obsluzonych"""
        self.liczba_obsluzonych += klieci


# egzemplarz
restauracja_1 = Restauracja('barcelona','kuchnia katalonska')

# wyswietlenie liczby obsluzonych klietow
restauracja_1.liczba_klientow()

# zmiana liczby obsluzonych klietow
restauracja_1.liczba_obsluzonych = 22
restauracja_1.liczba_klientow()

# wywolanie metody "obsluzeni_klieci"
restauracja_1.obsluzeni_klieci(15)
restauracja_1.liczba_klientow()
restauracja_1.obsluzeni_klieci(48)
restauracja_1.liczba_klientow()

# wywolanie metody inkrementacji
restauracja_1.obsluzeni_klieci(15)
restauracja_1.liczba_klientow()
restauracja_1.increment_liczby_obsluzonych(30)
restauracja_1.liczba_klientow()
restauracja_1.increment_liczby_obsluzonych(15)
restauracja_1.liczba_klientow()