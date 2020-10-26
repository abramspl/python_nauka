class User():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def dane(self):
        print(
            f'\nTo sa dane uzytkownika: {self.imie.upper()} {self.nazwisko.upper()}:'
            f'\n\tIMIE: {self.imie.title()}'
            f'\n\tNAZWISKO: {self.nazwisko.title()}')

    def powitanie(self):
        print(f'\nWitaj {self.imie.title()} {self.nazwisko.title()}!')

    def increment_prob_logowania(self,proba):
        self.proby_logowania += proba

    def reset_prob_logowania(self):
        self.proby_logowania = 0

    def info_logowanie(self):
        print(f'\nTo jest {self.proby_logowania} proba logowania!')

class Admin(User):
    def __init__(self,imie,nazwisko):
        super().__init__(imie,nazwisko)
        self.prawa = ['moze dodac postac','moze usunac postac','moze zbanowac uzytkownika']

    def pokaz_prawa(self):
        print('\nLista praw Administratora:')
        for prawo in self.prawa:
            print(f'\t* {prawo}')


gracz1 = Admin('lukasz','abrams')
gracz1.pokaz_prawa()
gracz1.dane()