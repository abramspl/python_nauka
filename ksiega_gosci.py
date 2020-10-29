tekst = '\nWitaj. Jak masz na imie? '
tekst += '\n(Aby zakonczyc program wpisz "exit")'
tekst += '\nImie: '

while True:
    gosc = input(tekst)

    if gosc == 'exit':
        break
    else:
        print(f'Dziekuje za odwiedziny {gosc.title()}')
        with open('ksiega_gosci.txt', 'a') as zapis:
            zapis.write(f'{gosc}\n')