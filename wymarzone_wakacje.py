odpowiedzi = {}
ankieta_active = True

while ankieta_active:
    imie = input('\nJak masz na imie? ')
    odpowiedz = input('Podaj jedno miejsce ktore bardzo chcesz odwiedzic: ')
    odpowiedzi[imie] = odpowiedz

    repeat = input('Czy jest kolejna osoba ktora chce udzielic odp w ankiecie? (tak/nie) ')
    if repeat == 'nie':
        ankieta_active = False

print('\n--- WYNIKI ANKIETY ---')
for imie,odpowiedz in odpowiedzi.items():
    print(f'{imie.title()} bardzo chce odwiedzic {odpowiedz.upper()}')