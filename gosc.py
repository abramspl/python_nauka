gosc = input('Witaj. Jak masz na imie? ')
print(f'Milo mi Cie poznac {gosc.title()}')

with open('gosc.txt','w') as zapis:
    zapis.write(gosc)