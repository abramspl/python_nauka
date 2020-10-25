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


lokal_1 = Restauracja('podlasiak','kuchania polska')

# wyswietlanie oddzielnie obu atrybutow

print('\nATRYBUTY "lokal_1":')
print(f'- "nazwa" - {lokal_1.nazwa}')
print(f'- "rodzaj" - {lokal_1.rodzaj}')

# wywolanie obu metod

print('\nMETODA PIERWSZA:')
lokal_1.info()
print('\nMETODA DRUGA:')
lokal_1.godziny()