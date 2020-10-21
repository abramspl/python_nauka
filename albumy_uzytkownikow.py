def make_album(artysta, album):
    zespol = {'ARTYSTA / ZESPOL': artysta, 'ALBUM': album}
    return  zespol

while True:
    print('\nPodaj ARTYSTE / ZESPOL i ALBUM:')
    print('(Wpisz "q" aby zakonczyc prace programu)')

    pozycja1 = input('ARTYSTA / ZESPOL: ')
    if pozycja1 == 'q':
        break
    pozycja2 = input('ALBUM: ')
    if pozycja2 == 'q':
        break

    dane = make_album(pozycja1, pozycja2)
    print(f'\n--- Dodano do bazy danych: ---\n{dane}')