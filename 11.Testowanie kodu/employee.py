class Employee():
	"""Tworzy profil pracownika"""

	def __init__(self, f_name, l_name, salary):
		"""Pobiera imię i nazwisko i roczną pensję"""
		self.first = f_name.title()
		self.second = l_name.title()# Przetworzenie informacji o repozytoriach.
		self.salary = salary

	def give_raise(self, amount=5_000):
		"""Zwiększa roczne wynagrodzenie o podaną kwotę (domyślnie o 5000 zł)"""
		self.salary += amount
		print(f"Podniesiono pensję pracownika o {amount}.")
		

