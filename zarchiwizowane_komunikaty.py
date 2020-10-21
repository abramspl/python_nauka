komunikaty = ['Mam na imie Lukasz', 'Moja ksywa to Abrams', 'Usze sie programowac']
wyslane_wiadomosci = []

def wyslac_wiadomosc(komunikaty, wyslane_wiadomosci):
    while komunikaty:
        komunikat = komunikaty.pop()
        print(f'Wysylam wiadomosc: {komunikat}')
        wyslane_wiadomosci.append(komunikat)

def wyslane(wyslane_wiadomosci):
    print('\nPonizsze wiadomosci zostaly wyslane:')
    for wyslana in wyslane_wiadomosci:
        print(f'\t- {wyslana}')

wyslac_wiadomosc(komunikaty[:],wyslane_wiadomosci)
print(f'\nLista "komunikaty" nie zostala zmieniona:\n{komunikaty}')