trzecie=[]
for wartosc in range(3,31):
	trzecia = wartosc**3
	trzecie.append(trzecia)
print(trzecie,'\n')

# inna opcja kodu

trzecie=[]
for wartosc in range(3,31):
	trzecie.append(wartosc**3)
print(trzecie,'\n')

# jeszcze inna opcja kodu

trzecie=[wartosc**3 for wartosc in range(3,31)]
print(trzecie,'\n')