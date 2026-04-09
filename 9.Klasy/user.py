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