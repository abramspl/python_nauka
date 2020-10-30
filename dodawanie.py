print('\nPodaj dwie liczby ktore chcesz dodac.')

warosc1 = input('\nPierwsza liczba: ')
warosc2 = input('Druga liczba: ')

try:
    suma = int(warosc1) + int(warosc2)
except ValueError:
    print('Zostala podana nieprawislowa wartosc liczby!')
else:
    print(f'Wynik: {suma}')