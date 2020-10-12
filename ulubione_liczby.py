liczby = {
	'tomek': [5,6,18],
	'darek': [76,13,7],
	'piotrek:': [11],
	'paulina': [2,100],
	'dawid': [103,4,8],
}

for osoba in liczby:
	print(f'\n{osoba.title()} i jego ulubione liczby:')
	for liczba in liczby[osoba]:
		print(liczba)

# lub taka wersja
for osoba,liczba in liczby.items():
	print(f'\n{osoba.title()} i jego liczby:')
	print(liczba)