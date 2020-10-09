urzytkownicy = []
if urzytkownicy:
	for urzytkownik in urzytkownicy:
		if urzytkownik == 'admin':
			print(f'Witaj {urzytkownik.upper()}! Czy chcesz przejrzec dzisiejszy raport?')
		else:
			print(f'Witaj {urzytkownik.title()}! Zostales zalogowany!')
else:
	print('Brak urzytkownikow')