def koszulka(rozmiar, tekst):
    """"Wyswietla wybrany rozmiar koszulki oraz tekst nadruku"""
    print(f'\nTwoja wielkosc koszulki to: {rozmiar.upper()}')
    print(f'Oto tekst nadruku na koszulce:\n--- {tekst.upper()} ---')

koszulka('xl','Moj ulubiony jezyk to Python')
koszulka(tekst='tak to wlasnie ja hehe',rozmiar='xxl')