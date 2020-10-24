def samochod(marka, model, **opcje):
    opcje['MARKA'] = marka
    opcje['MODEL'] = model
    return opcje

audi = samochod('audi', 'a3', kolor='srebrny', silnik=1.8)
print(audi)