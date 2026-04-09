filename = 'guests.txt'

with open(filename, 'w') as file_object:
	name = input("Proszę wprowadzić swoje imię: ")
	file_object.write(name)