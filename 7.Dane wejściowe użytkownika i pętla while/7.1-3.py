#7.1
print("7.1")

car = input("Witaj, jakiej marki samochód chciałbyś wypożyczyć? ")
print(f"Sprawdzam czy mamy dostępny samochód marki {car}...")

#7.2
print("\n7.2")

reservation = input("Witamy w naszej restauracji. Na ile osób zarezerwować państwu stolik? ")

reservation = int(reservation)

if reservation > 8:
	print("Będziesz musiał zaczekać, ponieważ ilość osób jest większa od 8.")
else:
	print("Zarezerwowano dla ciebie stolik. Do zobaczenia!")


#7.3
print("\n7.3")

number = input("Wprowadź dowolną liczbę: ")
number = int(number)

if number % 10 == 0:
	print("Twoja liczba jest wielokrotnością liczby 10!!")
else:
	print("Twoja liczba nie jest wielokrotnością liczby 10!!")