class Restauracja():
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def info(self):
        print(f'\nJest to restauracja o nazwie: {self.nazwa.title()}')
        print(f'Jej specjalizacja jest {self.rodzaj.upper()}')

    def godziny(self):
        print('\nGodziny funkcjonowania restauracji:')
        print('\t* PON - PIA (12-22)\n\t* SOB - NDZ (12-23)')


# trzy rozne egzemplarze
lokal_1 = Restauracja('Bella','kuchnia wloska')
lokal_2 = Restauracja('podlasiak','kuchnia polska')
lokal_3 = Restauracja('pekin','kuchnia orientalna')

# wywolanie metody 'info' dla kazdego egzemplarza
lokal_1.info()
lokal_2.info()
lokal_3.info()