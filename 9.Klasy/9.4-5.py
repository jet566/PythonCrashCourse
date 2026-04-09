#9.4
print("9.4")

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicjalizacja atrybutów restaurant_name i cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		"""Opisuje restaurację-nazwa i typ kuchni"""
		print(f"Restauracja nazywa się {self.restaurant_name.title()}, oraz serwuje dania kuchni {self.cuisine_type.title()}.")
	def open_restaurant(self):
		"""Wyświetla informację o godzinach pracy restauracji"""
		print(f"Restauracja {self.restaurant_name.title()} jest otwarta w godzinach 10-20 od wtorku do niedzieli.")
	def set_number_served(self, served):
		"""Ustawianie liczby obsłużonych klientów"""
		self.number_served = served
		print(f"\nLiczba klientów obsłużonych przez restaurację: {self.number_served}.")
	def increment_number_served(self, clients):
		"""Inkrementacja liczby obsłużonych klientów"""
		self.number_served += clients
		print(f"Liczba obsłużonych klientów w ciągu dnia roboczego: {self.number_served}.")


restaurant = Restaurant('Ha-noi', 'Azjatyckiej')

print(f"Liczba klientów obsłużonych przez restaurację: {restaurant.number_served}.")

restaurant.number_served = 20
print(f"Liczba klientów obsłużonych przez restaurację: {restaurant.number_served}.")

restaurant.set_number_served(100)

restaurant.increment_number_served(2)
restaurant.increment_number_served(29)
restaurant.increment_number_served(105)


#9.5
print("\n9.5")

class User():
	def __init__(self, first_name, last_name, age, date_of_birth):
		"""Inicjalizacja atrybutów first_name, last_name, age i date_of_birth"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.date_of_birth = date_of_birth
		self.login_attempts = 0
	def describe_user(self):
		"""Wyświetla podsumowanie informacji zebranych o użytkowniku"""
		print(f"Użytkownik nazywa się {self.first_name.title()} {self.last_name.title()} ma {self.age} lat oraz urodził/a się {self.date_of_birth} roku.")
	def greet_user(self):
		"""Wyświetla użytkownikowi spersonalizowane powitanie"""
		print(f"Witaj {self.first_name.title()}, jak się masz?")
	def increment_login_attempts(self, attempts):
		"""Metoda pozwalająca na inkrementację wartości login_attempts o 1"""
		if attempts == 1:
			self.login_attempts += 1
		else:
			print("Wartość prób logowania można zwiększyć tylko o 1!")
	def reset_login_attempts(self):
		"""Metoda zerująca wartość login_attempts"""
		self.login_attempts = 0


my_user = User('Igor', 'Kołodziejczyk', '19', '16.10.2003')

my_user.increment_login_attempts(1)
my_user.increment_login_attempts(2)
my_user.increment_login_attempts(0)
my_user.increment_login_attempts(-1)
my_user.increment_login_attempts(1)
my_user.increment_login_attempts(1)
print(f"Ilość prób logowania użytkownika: {my_user.login_attempts}.")

my_user.reset_login_attempts()
print(f"Ilość prób logowania użytkownika: {my_user.login_attempts}.")


