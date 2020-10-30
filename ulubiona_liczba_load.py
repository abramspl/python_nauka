import json

filename = 'ulubiona_liczba.json'

with open(filename) as f:
    liczba = json.load(f)
    print(f'\nTwoja ulubiona liczba to: {liczba}')