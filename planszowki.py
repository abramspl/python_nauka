filename = 'spis_gier.txt'

print(f'\n\t*** Witaj w programie do zapisywania kolekcji gier planszowych ***')

# Prostackie menu.
opcje = input(f'\n* Wybierz (1) aby dodac gre.'
              f'\n* Wybierz (2) aby zobaczyc liste gier.'
              f'\n* Twoj wybor: ')

flaga_aktywna1 = True

if opcje == '1':
    # Petla do wprowadzania danych i zapisu w pliku txt.
    while flaga_aktywna1:
        tytul_gry = input('\n* Podaj tytul gry: ')
        gatunek_gry = input('* Jaki to gatunek: ')
        liczba_graczy = input('* Podaj liczbe graczy: ')
        print(f'\n\t*** Gra "{tytul_gry.title()}" zostala dodana do listy ***')

        # Odczyt i dodanie kolejnego wpisu do pliku txt.
        with open(filename, 'a') as f:
            f.write(f'Gra: {tytul_gry.title()} * Gatunek: {gatunek_gry} * Liczba graczy: {liczba_graczy}\n')

        pytanie1 = input('\n* Czy chcesz dodac kolejna gre? (t/n): ')
        if pytanie1 == 'n':
            flaga_aktywna1 = False

            pytanie2 = input('* Czy chcesz zobaczyc aktualna liste gier? (t/n): ')
            if pytanie2 == 't':
                print('\n\t*** Aktualny spis Gier ***')
                with open(filename) as f:
                    zawartosc = f.read()
                print(f'\n{zawartosc}')
            else:
                print('\nProgram zostal zakonczony.')
                break

elif opcje == '2':
    print('\n\t*** Aktualny spis Gier ***')
    with open(filename) as f:
        zawartosc = f.read()
    print(f'\n{zawartosc}')

else:
    print(f'\nWybrana opcja jest nieprawidlowa!!!')
    print('Program zostal zakonczony.')

# Konsola czeka na dane, nastepnie zamknie okno z programem.
input()