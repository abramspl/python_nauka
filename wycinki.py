gracze=['piotr','lukasz','paulina','maciek','kuba']
print('Dzisiaj w gry planszowe beda grac nastepujacy gracze:\n')
for gracz in gracze:
	print(gracz.title())

print('\nPierwsza trojka graczy to:')
print(gracze[0:3])

print('\nTrzej srodkowi gracze to:')
print(gracze[1:4])

print('\nOstatnia trojka to:')
print(gracze[-3:])