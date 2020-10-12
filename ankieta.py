ankieta = {
	'tomek': 'python',
	'ania': 'java',
	'paulina': 'c',
	'piotrek': 'ruby',
}
lista_osob = ['janek','tomek','darek','piotrek']

for imie in lista_osob:
	if imie not in ankieta.keys():
		print(f'{imie.title()} prosze wez udzial w ankiecie')
	else:
		print(f'{imie.title()} dziekuje Ci za udzial w ankiecie')