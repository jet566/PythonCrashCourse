filename = 'answers.txt'
entry = 0

while True:
	entry += 1 
	with open(filename, 'a') as file_object:
		print("(Aby przerwać działanie programu wybierz 'q')")
		name = input(f"Proszę wprowadź swoje imię: ")
		if name == 'q':
			break
		else:
			print(f"Dlaczego lubisz programowanie {name.title()}?")
			answer = input(f"Odpowiedź: ")
			file_object.write(f"{entry}.) {name.title()} lubi programowanie... {answer}\n")
			print("Dziękujemy za twą odpowiedź!")

