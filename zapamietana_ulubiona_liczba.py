import json

# Wczytanie liczby z pliku jesli zostala ona wczesniej zapisana
# W przeciwnym razie pytamy o ulubiona liczbe i zapisujemy w pliku

filname = 'zapamietana_ulubiona_liczba.json'

try:
    with open(filname) as f:
        liczba = json.load(f)
except FileNotFoundError:
    liczba = int(input('\nPodaj swoja ulubiona liczbe: '))
    with open(filname,'w') as f:
        json.dump(liczba,f)
        print('Twoja ulubiona liczba zostala zapisana poprawnie.')
else:
    print(f'\nTo jest twoja ulubiona liczba: {liczba}')