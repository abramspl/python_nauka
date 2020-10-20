oferta_kanpki = ['serowa','warzywna','rybna','drobiowa','mix']
gotowe_kanapki = []

while oferta_kanpki:
    gotowa_kanapka = oferta_kanpki.pop()
    print(f'Kanapka {gotowa_kanapka.upper()} jest w przygotowaniu!')
    gotowe_kanapki.append(gotowa_kanapka)

print('\nWybrane kanapki sa gotowe:')
for gotowa_kanapka in gotowe_kanapki:
    print(gotowa_kanapka.upper())