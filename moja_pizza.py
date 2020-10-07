pizze=['klasyczna','miesna','serowa']

for pizza in pizze:
	print(f'Jedna z moich ulubionych pizzy, jest pizza {pizza.upper()}.')
print('\nPizza to jedno z moich ulubionych dan\n')

friend_pizza=pizze[:]

pizze.append('hawajska')
friend_pizza.append('bbq')

print(f'Moje ulubione pizze to: {pizze}')
print(f'Moi znajomi wola pizze: {friend_pizza}\n')

print('Moje ulubione pizze to: ')
for pizza in pizze:
	print(pizza.title())

print('\nUlubione pizze moich znajomych to: ')
for pizza in friend_pizza:
	print(pizza.title())