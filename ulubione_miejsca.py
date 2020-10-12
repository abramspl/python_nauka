ulubione_miejsca = {
	'tomek':['warszawa','podlasie','zakopane'],
	'lukasz':['podlasie','bieszczady','mazury'],
	'janek':['litwa','francja','polska']
}

for imie in ulubione_miejsca:
	print(f'\nUlubione miejsca {imie.title()} sa:')
	for miejsca in ulubione_miejsca[imie]:
		print(miejsca.upper())