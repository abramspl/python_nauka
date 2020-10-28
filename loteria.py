from random import choice

gra = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']

losowanie = choice(gra),choice(gra),choice(gra),choice(gra)

moj_kupon = (1,2,7,'A')

if losowanie == moj_kupon:
    print(f'\nWylosowano nastepujacy zestaw: {losowanie}')
    print('Wygrales!!!')
else:
    print(f'\nWylosowano nastepujacy zestaw: {losowanie}')
    print('Probuj dalej!!!')