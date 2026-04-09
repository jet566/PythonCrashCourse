print("-----Program dodawający dwie liczby-----")

while True:
	print("(Naciśnij 'q' aby zakończyć działanie programu)")
	try:
		first_number = input("\nWprowadź pierwszą liczbę: ")
		if first_number == 'q':
			break

		second_number = input("Wprowadź drugą liczbę: ")
		if second_number == 'q':
			break

		answer = int(first_number) + int(second_number)

	except ValueError:
		print("Błąd! Program przyjmuje tylko liczby.")

	else:
		print(f"Wynik z dodawania {first_number} + {second_number} = {answer}\n")

