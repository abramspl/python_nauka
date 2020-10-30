def ilosc_slow(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            zawartosc = f.read()
    except FileNotFoundError:
        print(f'\nPlik {filename} nie istnieje!')
    else:
        slowa = zawartosc.split()
        liczba_slow = len(slowa)
        print(f'\nPlik {filename} zawiera {liczba_slow} slow.')

def slowo(filename,wyraz):
    try:
        with open(filename, encoding='utf-8') as f:
            zawartosc = f.read()
    except FileNotFoundError:
        print(f'\nPlik {filename} nie istnieje!')
    else:
        dane_slowo = wyraz
        dane_slowo = zawartosc.lower().count(dane_slowo)
        print(f'Slowo "{wyraz}" wystepuje w tekscie {dane_slowo} razy.')


filename = 'najczesciej_wystepujace_slowa.txt'

ilosc_slow(filename)
slowo(filename,'hej')
slowo(filename,'sokoły')