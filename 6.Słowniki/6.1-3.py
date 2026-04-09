#6.1
print("6.1")
person = {'first_name': 'Vanessa' , 'last_name': 'Konkiel' , 'age': '20' , 'city': 'Zgorzelec'}
print(person)

#6.2
print("\n6.2")
favourite_numbers = {
	'Vanessa': '12',
	'Igor': '7',
	'Oliwier': '69',
	'Natalia': '53',
	'Kamil': '1',
}
print(favourite_numbers)

#6.3
print("\n6.3")
glosariusz = {
	'Iteracja': 'Powtarzanie tej samej operacji aż do spełnienia warunku',
	'Test warunkowy': 'Sprawdzenie czy spełniono dany warunek',
	'Lista': 'Lista nieuporządkowanych informacji',
	'Krotka': 'Lista bez możliwości modyfikacji',
	'Pętla': 'Powtarzanie',
}
for key, value in glosariusz.items():
	print(f"\n{key}:\t{value}")