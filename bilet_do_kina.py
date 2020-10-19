tekst = 'Witaj w naszym kinie. Podaj swoj wiek a ja podam ci cene biletu: '
wiek = input(tekst)
wiek = int(wiek)

if wiek < 3:
    print('Bilet jest bezplatny. Milego seansu.')
elif wiek <= 12:
    print('Cena biltu to 10zł. Milego seansu.')
else:
    print('Cena biletu to 15zl. Milego seansu')

# v2

tekst = '\nWitaj w naszym kinie. Podaj swoj wiek a ja podam ci cene biletu: '
tekst += '\n(Aby zakonczyc wpisz liczbe "0")\nWiek: '

while True:
    wiek = input(tekst)
    wiek = int(wiek)

    if wiek == 0:
        break
    elif wiek < 3:
        print('Bilet jest bezplatny.')
    elif wiek <= 12:
        print('Cena biltu to 10zł. Milego seansu.')
    else:
        print('Cena biletu to 15zl. Milego seansu')