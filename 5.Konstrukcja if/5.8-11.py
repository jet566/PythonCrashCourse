#5.8
print("5.8")

users = ['admin' , 'bolek' , 'lolek' , 'maciek' , 'agata']
for user in users:
	if user == 'admin':
		print(f"Witaj, {user}! Czy chcesz przejrzeć dzisiejszy raport?")
	else:
		print(f"Witaj, {user}! Dziękujemy że się ponownie zalogowałeś!")

#5.9
print("\n5.9")

users = []
if users:
	for user in users:
		if user == 'admin':
			print(f"Witaj, {user}! Czy chcesz przejrzeć dzisiejszy raport?")
		else:
			print(f"Witaj, {user}! Dziękujemy że się ponownie zalogowałeś!")
else:
	print("Musimy znaleźć jakichś użytkowników!")

#5.10
print("\n5.10")

current_users = ['mariusz' , 'maniek' , 'Vanessa' , 'bolek' , 'lolek']
new_users = ['vanessa' , 'kamil' , 'jacek' , 'igor' , 'joanna']
current_users_copy = [item.lower() for item in current_users]

for user in new_users:
	if user.lower() in current_users_copy:
		print(f"Przepraszamy, nazwa {user} jest już zajęta! Wybierz inną nazwę!")
	else:
		print(f"{user.title()} ta nazwa jest wolna! Możesz jej użyć!")

#5.11
print("\n5.11")

numbers = [1 , 2 , 3 , 4, 5 , 6, 7, 8 , 9]
for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")