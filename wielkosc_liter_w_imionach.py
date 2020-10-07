imie='lukasz'
print('Witaj',imie.title(),'! Jak sie dzisiaj masz?')

imie='tomek'
print(imie.lower())
print(imie.upper())
print(imie.title())

print("\tAlbert Einstein powiedzial, kiedys:\n\t'Osoba, ktora nigdy nie popelnia bledu, jest kims, kto nigdy nie probowal, niczego nowego'")

imie='Albert'
nazwisko='Einstein'
famous_person=f'{imie} {nazwisko}'
message=f"\t{famous_person}, powiedzial, kiedys:\n\t'Osoba, ktora nigdy nie popelnia bledu, jest kims, kto nigdy nie probowal, niczego nowego'"
print(message)

imie=' Janek '

print(imie.lstrip())
print(imie.rstrip())
print(imie.strip())