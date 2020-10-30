try:
    with open('psy.txt') as f:
        zawartosc1 = f.read()
except FileNotFoundError:
    print('\nBrak takiego pliku!')
else:
    print(f'\nZawartosc pliku "txt":\n{zawartosc1}')

try:
    with open('koty.txt') as f:
        zawartosc2 = f.read()
except FileNotFoundError:
    print('\nBrak takiego pliku!')
else:
    print(f'\nZawartosc pliku "txt":\n{zawartosc2}')