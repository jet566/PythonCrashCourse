import json

filename = 'favourite_number.json'

def get_stored_number():
	"""Pobiera ulubioną liczbę z pliku, o ile taki istnieje"""
	try:
		with open(filename) as f:
			favourite_number = json.load(f)

	except FileNotFoundError:
		return None

	else:
		return favourite_number

def show_favourite_number():
	"""Pokazuje ulubioną liczbę"""
	number = get_stored_number()
	if number:
		print(f"Znam twoją ulubioną liczbę, to: {number}")
	else:
		favourite_number = int(input("Podaj swoją ulubioną liczbę: "))
		save_number(favourite_number)

def save_number(favourite_number):
	"""Zapisuje ulubioną liczbę użytkownika"""
	with open(filename, 'w') as f:
			json.dump(favourite_number, f)
			print("Dzięki, zapamiętam ją.")

show_favourite_number()

