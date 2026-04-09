#7.10

places = {}
polling_active = True

while polling_active:
	name = input("\nJak masz na imię? ")
	place = input("Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał?: ")
	places[name] = place
	repeat = input("Dziękujemy za odpowiedź! Czy jest jeszcze ktoś kto chce wziąć udział w ankiecie? (tak/nie) ")

	if repeat == 'nie':
		polling_active = False

print("\n---Wyniki ankiety ---")
for name, place in places.items():
	print(f"{name.title()} chciałby pojechać do {place.title()}.")

