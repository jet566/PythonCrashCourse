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
