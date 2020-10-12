miasta = {
	'warszawa': {
		'kraj':'polska',
		'populacja':700_000,
		'info':'stolica'
	},
	'ateny': {
		'kraj':'grecja',
		'populacja':5_700_000,
		'info':'stolica'
	},
	'grodno': {
		'kraj':'bialorus',
		'populacja':200_000,
		'info':'miasto przygraniczne'
	}
}
for miasto, dane in miasta.items():
	print(f'\n{miasto.upper()}')
	for informacje, opis in dane.items():
		print(f'\t{informacje.upper()}: {opis}')