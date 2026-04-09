#6.7
print("6.7")

person_0 = {'first_name': 'Vanessa' , 'last_name': 'Konkiel' , 'age': '20' , 'city': 'Zgorzelec'}
person_1 = {'first_name': 'Igor' , 'last_name': 'Kołodziejczyk' , 'age': '19' , 'city': 'Sulików'}
person_2 = {'first_name': 'Kamil' , 'last_name': 'Łapiński' , 'age': '19' , 'city': 'Zgorzelec'}

people = [person_0 , person_1 , person_2]

for person in people:
	print(f"Imię: {person['first_name']}, Nazwisko: {person['last_name']}, Wiek: {person['age']}, Miejsce zamieszkania: {person['city']}.\n")

#6.8
print("6.8")

burek = {
	'rodzaj': 'pies',
	'rasa': 'doberman',
	'wiek': '12',
}

maniek = {
	'rodzaj': 'pies',
	'rasa': 'lablador',
	'wiek': '5',
}

obsraniec = {
	'rodzaj': 'kot',
	'rasa': 'mańkun',
	'wiek': '3',
}

spajki = {
	'rodzaj': 'pies',
	'rasa': 'chuj wie',
	'wiek': '16',
}

pets = [burek, maniek, obsraniec, spajki]

for pet in pets:
	print(f"Zwierze: {pet['rodzaj'].title()}, Rasa: {pet['rasa'].title()}, Wiek: {pet['wiek']}.\n")

#6.9
print("\n6.9")

favourite_places = {
	'igor': ['Chorwacja', 'Grecja', 'Malediwy',],
	'vanessa': ['Grecja', 'Berzdorf', 'Zgorzelec'],
	'asia': ['Chorwacja', 'Turcja', 'Mielno'],
}

for name, places in favourite_places.items():
	print(f"\nUlubione miejsca {name.title()}, to: ")
	for place in places:
		print(f"\t{place.title()}")

#6.10
print("\n6.10")

favourite_numbers = {
	'Vanessa': ['12', '20'],
	'Igor': ['7', '40'],
	'Oliwier': ['7.5' , '69'],
	'Natalia': ['25', '53'],
	'Kamil': ['47','1'],
}

for person, numbers in favourite_numbers.items():
	print(f"\nUlubione liczby {person}, to:")
	for number in numbers:
		print(f"\t{number}")

#6.11
print("\n6.11")

cities = {
	'Warsaw': {
	'country': 'Poland',
	'population': '1.794.000',
	'fact': 'has been rebuilt after II world war',
	},
	'London': {
	'country': 'Great Britain',
	'population': '8.982.000',
	'fact': 'is capital of the United Kingdom',
	},
	'Madrid': {
	'country': 'Spain',
	'population': '6.700.000',
	'fact': 'is the second-largest city in European Union',
	},
}

for city, info in cities.items():
	print(f"\n{city} is a city in {info['country']} and has the population of {info['population']}. Did you know that {city} {info['fact']}?")










