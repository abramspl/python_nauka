class Car():
    def __init__(self,marka,model,rok):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.aktualny_przebieg = 0

    def car_info(self):
        long_name = f'{self.rok} {self.marka} {self.model}'
        return long_name.title()

    def przebieg_info(self):
        print(f'Aktualny przebieg to {self.aktualny_przebieg} km.')

    def update_przebieg(self,kilometry):
        if kilometry >= self.aktualny_przebieg:
            self.aktualny_przebieg = kilometry
        else:
            print('Nie mozna cofac licznika!!!')

    def incremente_przebieg(self,kilometry):
        self.aktualny_przebieg += kilometry

class Bateria():
    def __init__(self,wielkosc_baterii=75):
        self.wielkosc_baterii = wielkosc_baterii

    def bateria_info(self):
        print(f'Ten samochod ma akumulator o pojemnosci {self.wielkosc_baterii} kWh.')

    def zasieg_info(self):
        if self.wielkosc_baterii == 75:
            zasieg = 260
        elif self.wielkosc_baterii == 100:
            zasieg = 315

        print(f'\nZasieg tego samochodu wynosi okolo {zasieg} km'
              f' po pelnym naladowaniu akumulatora.')

    def ulepszenie_baterii(self):
        if self.wielkosc_baterii < 100:
            self.wielkosc_baterii = 100

class ElectricCar(Car):
    def __init__(self,marka,model,rok):
        super().__init__(marka,model,rok)
        self.bateria = Bateria()


tesla1 = ElectricCar('tesla','rxs',2020)

tesla1.bateria.zasieg_info()
tesla1.bateria.ulepszenie_baterii()
tesla1.bateria.zasieg_info()