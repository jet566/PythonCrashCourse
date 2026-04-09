#9.8
print("9.8")


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


mariusz = Admin('Mariusz', 'Pudzianowski', '50', '21.37.1974')
mariusz_privileges = [
	'podniesienie głazu 300kg', 
	'zjedzenie całego obiadku u babci (nigdy nie zostawia mięska)', 
	'wypicie 4 browarów po robocie',
	]	

mariusz.describe_user()

mariusz.privileges.privileges = mariusz_privileges
mariusz.privileges.show_privileges()


#9.9
print("9.9")

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
    	"""Check battery capacity and set it on 100 if it is different"""
    	if self.battery_size == 75:
    		self.battery_size = 100
    		print("The battery size has been set to 100.")
    	else:
    		print("The battery size has not been changed.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

tesla = ElectricCar('Tesla', 'Model S', '2023')
print(tesla.get_descriptive_name())

tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()