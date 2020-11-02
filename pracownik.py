class Pracownik():

    def __init__(self,imie,nazwisko,wynagrodzenie_roczne):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_roczne = wynagrodzenie_roczne

    def dac_podwyzke(self,podwyzka=5000):
        self.wynagrodzenie_roczne += podwyzka

# pracownik1 = Pracownik('lukasz','abrams',1000)
# print(pracownik1.dane_pracownik())