import json

filename = 'favourite_number.json'
favourite_number = input("Podaj swoją ulubioną liczbę: ")

with open(filename, 'w') as f:
	json.dump(favourite_number, f)
	print("Dzięki, zapamiętam ją.")