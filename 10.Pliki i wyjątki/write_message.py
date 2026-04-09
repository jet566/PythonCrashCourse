filename = 'programming.txt'

#	with open(filename, 'w') as file_object:
#		file_object.write(f"Uwielbiam programować {str(12)}\n")
#		file_object.write(f"Uwielbiam tworzyć gry")

with open(filename, 'a') as file_object:
	file_object.write(f"\nUwielbiam odnajdywać pojedyncze elementy w ogromnych zbiorach danych")
	file_object.write(f"\nUwielbiam tworzyć aplikacje uruchamiane w przeglądarce internetowej")