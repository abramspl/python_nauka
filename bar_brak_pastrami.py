oferta_kanpki = ['serowa','pastrami','warzywna','pastrami','rybna','drobiowa','mix','pastrami']
gotowe_kanapki = []

print('\nPrzepraszamy ale aktualnie brak kanpki "PASTRAMI"')

while 'pastrami' in oferta_kanpki:
    oferta_kanpki.remove('pastrami')

print('\nAktualna oferta kanpkowa to:')
for kanapka in oferta_kanpki:
    print(f'- {kanapka.upper()}')

print('SMACZNEGO!!!\n')

while oferta_kanpki:
    gotowa_kanapka = oferta_kanpki.pop()
    print(f'Kanapka {gotowa_kanapka.upper()} jest w przygotowaniu!')
    gotowe_kanapki.append(gotowa_kanapka)

print('\nWybrane kanapki sa gotowe:')
for gotowa_kanapka in gotowe_kanapki:
    print(gotowa_kanapka.upper())

print('\nSMACZNEGO!!!\n')