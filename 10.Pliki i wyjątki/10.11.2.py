import json

filename = 'favourite_number.json'

with open(filename) as f:
	number = json.load(f)

print(f"Znam twoją ulubioną liczbę, to: {number}")