#9.1
print("9.1")

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicjalizacja atrybutów restaurant_name i cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		"""Opisuje restaurację-nazwa i typ kuchni"""
		print(f"Restauracja nazywa się {self.restaurant_name.title()}, oraz serwuje dania kuchni {self.cuisine_type.title()}.")
	def open_restaurant(self):
		"""Wyświetla informację o godzinach pracy restauracji"""
		print(f"Restauracja {self.restaurant_name.title()} jest otwarta w godzinach 10-20 od wtorku do niedzieli.")


restaurant = Restaurant('Ha-noi', 'Azjatyckiej')
print(
	f"Atrybuty:\n\t{restaurant.restaurant_name.title()}\n\t{restaurant.cuisine_type.title()}"
	)
restaurant.describe_restaurant()
restaurant.open_restaurant()


#9.2
print("\n9.2")

my_restaurant = Restaurant('Speluno', 'Polskiej')
oriental_restaurant = Restaurant('Asia Express', 'Orientalnej')
italian_restaurant = Restaurant("A'more", 'Włoskiej')

my_restaurant.describe_restaurant()
oriental_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()


#9.3
print("\n9.3")

class User():
	def __init__(self, first_name, last_name, age, date_of_birth):
		"""Inicjalizacja atrybutów first_name, last_name, age i date_of_birth"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.date_of_birth = date_of_birth
	def describe_user(self):
		"""Wyświetla podsumowanie informacji zebranych o użytkowniku"""
		print(f"Użytkownik nazywa się {self.first_name.title()} {self.last_name.title()} ma {self.age} lat oraz urodził/a się {self.date_of_birth} roku.")
	def greet_user(self):
		"""Wyświetla użytkownikowi spersonalizowane powitanie"""
		print(f"Witaj {self.first_name.title()}, jak się masz?")

my_user = User('Igor', 'Kołodziejczyk', '19', '16.10.2003')
user1 = User('Jadwiga', 'Mikołajczykówna', '48', '05.03.1975')
user2 = User('Jerzy', 'Krajewski', '100', '01.01.1923')
user3 = User('Janusz', 'Smith', '25', '08.12.1998')

my_user.greet_user()
my_user.describe_user()

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

