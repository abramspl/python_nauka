class User():
    def __init__(self, imie, nazwisko, wiek, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.proby_logowania = 0

    def dane(self):
        print(
            f'To sa dane uzytkownika: {self.imie.upper()} {self.nazwisko.upper()}:'
            f'\n\tIMIE: {self.imie.title()}'
            f'\n\tNAZWISKO: {self.nazwisko.title()}'
            f'\n\tWIEK: {self.wiek}'
            f'\n\tWZROST: {self.wzrost}'
            f'\n\tWAGA: {self.waga}')

    def powitanie(self):
        print(f'\nWitaj {self.imie.title()} {self.nazwisko.title()}!')

    def increment_prob_logowania(self,proba):
        self.proby_logowania += proba

    def reset_prob_logowania(self):
        self.proby_logowania = 0

    def info_logowanie(self):
        print(f'\nTo jest {self.proby_logowania} proba logowania!')


# egzemplarz
gracz1 = User('lukasz','abrams',18,170,80)

# testowanie dzialania metod "increment_prob_logowania" i "reset_prob_logowania"
gracz1.increment_prob_logowania(2)
print(gracz1.proby_logowania)
gracz1.increment_prob_logowania(7)
print(gracz1.proby_logowania)
gracz1.reset_prob_logowania()
print(gracz1.proby_logowania)

gracz1.increment_prob_logowania(2)
gracz1.info_logowanie()
gracz1.increment_prob_logowania(13)
gracz1.info_logowanie()
gracz1.reset_prob_logowania()
gracz1.info_logowanie()