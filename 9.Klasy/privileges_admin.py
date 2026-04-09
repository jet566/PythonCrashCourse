from user import User

class Admin(User):
	def __init__(self, first_name, last_name, age, date_of_birth):
		"""Inicjalizacja użytkownika"""
		super().__init__(first_name, last_name, age, date_of_birth)
		self.privileges = Privileges()

class Privileges():
	def __init__(self, privileges = []):
		"""Inicjalizacja atrybutu privileges"""
		self.privileges = privileges
	def show_privileges(self):
		"""Pokazuje uprawnienia administratora"""
		print(f"\nUżytkownik jest administratorem i jego uprawnienia to:")
		if self.privileges:
			for privilege in self.privileges:
				print(f"\t-{privilege}")
		else:
			print("- Ten użytkownik nie ma żadnych uprawnień.")