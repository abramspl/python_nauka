goscie = ['janek','gosia','tomek']

zaproszenie1=f'Czesc {goscie[0].title()}. Zapraszam cie na obiad.'
zaproszenie2=f'Czesc {goscie[1].title()}. Zapraszam cie na obiad.'
zaproszenie3=f'Czesc {goscie[2].title()}. Zapraszam cie na obiad.'

print(zaproszenie1)
print(zaproszenie2)
print(zaproszenie3)

rezygnacja=f'Niestety {goscie[2].title()} dzisiaj do nas nie dolaczy'
print(rezygnacja)

# usuwanie i dodanie nowego imienia do listy
del goscie[2]
goscie.insert(2,'darek')
zaproszenie3=f'Czesc {goscie[2].title()}. Zapraszam cie na obiad.'

print(zaproszenie1)
print(zaproszenie2)
print(zaproszenie3)

print('Huuuura! Udalo sie znalesc wiekszy stolik')

# dodanie nowych imion do listy
goscie.insert(0,'ania')
goscie.insert(2,'kasia')
goscie.append('grzesiek')

zaproszenie1=f'Czesc {goscie[0].title()}. Zapraszam cie na obiad.'
zaproszenie2=f'Czesc {goscie[1].title()}. Zapraszam cie na obiad.'
zaproszenie3=f'Czesc {goscie[2].title()}. Zapraszam cie na obiad.'
zaproszenie4=f'Czesc {goscie[3].title()}. Zapraszam cie na obiad.'
zaproszenie5=f'Czesc {goscie[4].title()}. Zapraszam cie na obiad.'
zaproszenie6=f'Czesc {goscie[5].title()}. Zapraszam cie na obiad.'

print(zaproszenie1)
print(zaproszenie2)
print(zaproszenie3)
print(zaproszenie4)
print(zaproszenie5)
print(zaproszenie6)