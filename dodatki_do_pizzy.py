prompt = '\nPodaj nazwe skladnika jaki ma byc dodany do pizzy:'
prompt += '\nNapisz "koniec", aby zakonczyc dodawanie skladnikow: '

while True:
    skladnik = input(prompt)

    if skladnik == 'koniec':
        break
    else:
        print(f'\t- {skladnik.upper()} zostal dodany do pizzy!')

# lub

active = True
while active:
    wiadomosc = input(prompt)

    if wiadomosc == 'koniec':
        active = False
    else:
        print(f'\t- {wiadomosc.upper()} zostal dodany do pizzy!')