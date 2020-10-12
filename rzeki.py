rzeki = {
	'wisla': 'polska',
	'nil': 'egipt',
	'amazonka': 'ameryka_po',
}

for rzeka, kraj in rzeki.items():
	print(f'{rzeka.title()} przeplywa przez kraj jakim jest {kraj.upper()}')

# petla wyswietla wszystkie rzeki - klucze slownika
for rzeka in rzeki.keys():
	print(rzeka.upper())

# petla wyswietla wszystkie kraje - wartosci slownika
for kraj in rzeki.values():
	print(kraj.title())