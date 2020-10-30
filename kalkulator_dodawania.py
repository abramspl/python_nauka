print('\nPodaj dwie liczby ktore chcesz dodac.')
print('(Wpisz "q" aby zakonczyc prace programu)')

while True:
    warosc1 = input('\nPierwsza liczba: ')
    if warosc1 == 'q':
        break
    warosc2 = input('Druga liczba: ')
    if warosc2 == 'q':
        break
    try:
        suma = int(warosc1) + int(warosc2)
    except ValueError:
        print('Zostala podana nieprawislowa wartosc liczby!')
    else:
        print(f'Wynik: {suma}')