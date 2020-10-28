from random import choice

gra = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
moj_kupon = (1,2,7,'A')

losowanie = choice(gra),choice(gra),choice(gra),choice(gra)
liczba_prob = 1

while losowanie != moj_kupon:
    losowanie = choice(gra),choice(gra),choice(gra),choice(gra)
    liczba_prob += 1
    if losowanie == moj_kupon:
        print(f'\nTym razem do wygrania potrzebowales {liczba_prob} prob!!!')