# v1 - odczytanie calego "plik1.txt"

print('\nWersja v1:')
with open('plik1.txt') as plik_txt:
    notatka = plik_txt.read()

print(notatka)

# v2 - wyswietlenie "plik1.txt" przez iteracje

print('\nWersja v2:')

notatka = 'plik1.txt'

with open(notatka) as plik_txt:
    for linia in plik_txt:
        print(linia)

# v3 - wyswietlenie "plik1.txt" przez umieszczenie wierszy na liscie
#      nastepnie przetworzenie listy poza blok "with"

print('\nWersja v3:')

notatka = 'plik1.txt'

with open(notatka) as plik_txt:
    linie = plik_txt.readlines()

for linia in linie:
    print(linia.rstrip())