"""Klasa, która będzie używana do zaprezentowania samochodu."""
class Car():
"""Prosta próba zaprezentowania samochodu."""
def __init__(self, make, model, year):
“””Inicjalizacja atrybutów opisujących samochód.”””
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
“””Zwrot elegancko sformatowanego opisu samochodu.”””
long_name = f”{self.year} {self.make} {self.model}”
return long_name.title()
def read_odometer(self):
“””Wyświetla informację o przebiegu samochodu.””