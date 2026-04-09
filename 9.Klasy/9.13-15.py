#9.13
print("9.13")

from random import randint

class Die():
	"""Symuluje kość do gry którą można rzucić"""
	def __init__(self, sides = 6):
		"""Inicjalizacja atrybutu sides z domyślną wartością"""
		self.sides = sides
	def roll_die(self, times = 1):
		"""Rzuca kostką, w zależności od liczby scianek"""
		self.times = times
		print(f"\nRzucasz kością {times} razy. Oto rezultat:")
		for time in range(1, times+1):
			print(f"\t-{randint(1, self.sides)}")

kosc6 = Die().roll_die(10)
kosc10 = Die(10).roll_die(10)
kosc20 = Die(20).roll_die(10)


#9.14
print("\n9.14")

from random import choice

series = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'a' , 'b' , 'c' , 'd')

winning_ticket = []
print("Zobaczmy jak wygląda dzisiejszy wygrywający kupon...")

while len(winning_ticket) < 4:
	pulled_item = choice(series)

	if pulled_item not in winning_ticket:
		winning_ticket.append(pulled_item)
		print(f"Wyciągnęliśmy {pulled_item}!")

print(f"Dzisiejszy wygrany kupon wygląda tak: {winning_ticket}")


#9.15
print("\n9.15")

print("Zobaczmy jak trudno wygrać na loterii...")

#	Nie chcemy aby wygrywające literki lub cyfry się powtarzały więc użyjemy
#	pętli while
def get_winning_ticket(possibilities):
	winning_ticket = []

	while len(winning_ticket) < 4:
		pulled_item = choice(possibilities)

		if pulled_item not in winning_ticket:
			winning_ticket.append(pulled_item)

	return winning_ticket

def check_ticket(my_ticket, winning_ticket):
	# Sprawdź wszystkie elementy w obecnym kuponie. Jeśli żadne nie znajduja sie w wygrywajacym kuponie zwroc False"""
	for element in my_ticket:
		if element not in winning_ticket:
			return False

	# Musimy mieć wygrywający kupon
	return True

def make_random_ticket(possibilities):
	ticket = []
	while len(ticket) < 4:
		pulled_item = choice(possibilities)

		if pulled_item not in ticket:
			ticket.append(pulled_item)

	return ticket

possibilities = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'a' , 'b' , 'c' , 'd')
plays = 0
winning_ticket = get_winning_ticket(possibilities)

won = False

while not won:
	new_ticket = make_random_ticket(possibilities)
	won = check_ticket(new_ticket, winning_ticket)
	plays += 1

if won:
	print(f"Gratulacjie udało ci się wygrać... za {plays} razem.")
	print(f"Twój kupon: {new_ticket}")

