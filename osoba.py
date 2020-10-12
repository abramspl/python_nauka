osoba = {'imie':'koziolek','nazwisko':'matolek','wiek':103,'miasto':'pacanowo'}

lokalizacja = osoba['miasto']
postac_imie = osoba['imie']
postac_naz = osoba['nazwisko']
wiek = osoba['wiek']

print(f'W miejscowosci {lokalizacja.title()}')
print(f'Mieszka {postac_imie.title()} {postac_naz.title()} i ma {wiek} lata')