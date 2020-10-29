notatka = 'plik1.txt'

with open(notatka) as plik_txt:
    for linia in plik_txt:
        print(linia.rstrip())

# zamiana slowa "Pythonie" na slowo "C"

print('\nZmiana slowa "Pythonie" na "C"')
with open(notatka) as plik_txt:
    linie = plik_txt.readlines()

zmiana = ''

for linia in linie:
    zmiana += linia.replace('Pythonie','C')

print(zmiana)