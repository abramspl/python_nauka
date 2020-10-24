def dane_profilu(imie, nazwisko, **inne_informacje):
    """Budowa slownika zawierajacego wszelkie informacje
    o uzytkowniku"""
    inne_informacje['imie'] = imie
    inne_informacje['nazwisko'] = nazwisko
    return inne_informacje

osoba1 = dane_profilu('lukasz','abrams',lokacja='choroszcz',wzrost=175,hobby='programowanie')
print(osoba1)