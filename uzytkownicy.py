class User():
    def __init__(self, imie, nazwisko, wiek, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga

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


# egzemplarze

osoba1 = User('lukasz','abrams',36,175,100)
osoba2 = User('jan','kowalski',50,180,78)
osoba3 = User('diego','ramirez',23,160,72)

# wywolanie metod dla kazdej osoby

osoba1.powitanie()
osoba1.dane()
osoba2.powitanie()
osoba2.dane()
osoba3.powitanie()
osoba3.dane()