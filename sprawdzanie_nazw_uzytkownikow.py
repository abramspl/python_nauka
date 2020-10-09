current_users = ['abrams','dymek','peter','pinek','zenek']
new_users = ['janek','antek','Abrams','tomek','PINEK']

for new_user in new_users:
	new_user = new_user.lower()
	if new_user in current_users:
		print('Ta nazwa uzytkownika jest juz zajeta!')
	else:
		print('Zostales dodany do listy uzytkownikow!')