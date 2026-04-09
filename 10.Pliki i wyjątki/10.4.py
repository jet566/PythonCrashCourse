filename = 'guest_book.txt'
entry = 0

while True:
	entry += 1
	with open(filename, 'a') as file_object:
		print("(Aby przerwać działanie programu wciśnij 'q')")
		name = input("Proszę wprowadź swoje imię: ")
		if name == 'q':
			break
		else:
			print(f"Witaj {name.title()}! Zostałeś wpisany do księgi gości.")
			file_object.write(f"{entry}.Wpisano {name.title()}\n")

