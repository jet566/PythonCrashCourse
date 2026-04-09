pizzas = ['Neapoletana' , 'Cztery sery' , 'Kebab' , 'Parmeńska']

friend_pizzas = pizzas[:]

pizzas.append('Foccacia')

friend_pizzas.append('Margharita')

print("Moje ulubione rodzaje pizzy to")
for pizza in pizzas:
	print(pizza)

print("Ulubione rodzaje pizzy mojego przyjaciela to: ")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
