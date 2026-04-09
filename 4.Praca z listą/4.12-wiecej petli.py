my_foods = ['pizza' , 'falafel' , 'ciasto z marchwi']
my_foods.append('canolo')

for my_food in my_foods:
	print(my_food)

friend_foods = my_foods[:]
friend_foods.append('foccacia')

for food in friend_foods:
	print(food)