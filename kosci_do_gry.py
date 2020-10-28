from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        wynik = randint(1,self.sides)
        print(wynik)

kosc1 = Die()
kosc1.sides = 20

kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()
kosc1.roll_die()