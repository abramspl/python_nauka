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

# dziedziczenie klasy "Restauracja"

class Budka_z_lodami(Restauracja):
    def __init__(self,nazwa,rodzaj):
        super().__init__(nazwa,rodzaj)
        self.smaki = ['smietankowy','czekoladowy','orzechowy']

    def lista_smakow(self):
        print('\nAktualnie w sprzedazy posiadamy nastepujace smaki:')
        for smak in self.smaki:
            print(f'\t* {smak.upper()}')


lody1 = Budka_z_lodami('mango','lody')
lody1.lista_smakow()