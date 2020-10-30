import json

filname = 'ulubiona_liczba.json'

liczba = int(input('\nPodaj swoja ulubiona liczbe: '))

with open(filname,'w') as f:
    json.dump(liczba,f)
    print('Twoja ulubiona liczba zostala zapisana.')