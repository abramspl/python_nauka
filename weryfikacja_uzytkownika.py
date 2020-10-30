import json

def odczyt_nazwy_urzytkownika():
    """Pobieranie imienia z pliku, o ile taki istnieje."""
    filename = 'imie_urzytkownika.json'
    try:
        with open(filename) as f:
            imie = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return imie

def powitanie_urzytkownika():
    """Powitanie urzytkownika z uzyciem jego imienia."""
    imie = odczyt_nazwy_urzytkownika()
    if imie:
        print(f'\nWitaj ponownie. Czy to jest twoje imie: {imie.title()}')
        odp = input('Wpisz "tak" lub "nie" jesli Twoje imie sie nie zgadza: ')
        if odp == 'tak':
            print(f'Witaj {imie.title()}!')
        elif odp == 'nie':
            imie = uzyskanie_nazwy_urzytkownika()
            print(f'Twoje imie zostalo zapisane. Witaj {imie.title()}!')
        else:
            print('Bledna odpowiedz. Sprobuj ponownie.')
            return powitanie_urzytkownika()

def uzyskanie_nazwy_urzytkownika():
    """
    Poproszenie uzytkownika, aby podal swoje imie,
    a nastepnie zapisanie tego imienia w pliku.
    """
    imie = input("\nJak masz na imie? ")
    filename = 'imie_urzytkownika.json'
    with open(filename,'w') as f:
        json.dump(imie,f)
    return imie

powitanie_urzytkownika()