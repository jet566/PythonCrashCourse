from city_functions import get_formatted_place
import unittest

class PlaceTestCase(unittest.TestCase):
	"""Testy dla programu city_functions.py"""

	def test_city_country(self):
		"""Czy dane w postaci 'Warsaw, Poland' są obsługiwane prawidłowo?"""
		formatted_place = get_formatted_place('warsaw', 'poland')
		self.assertEqual(formatted_place, 'Warsaw, Poland - population ')

	def test_city_country_population(self):
		"""Czy dane w postaci 'Santiago, Chile - population 5000000' są obsługiwane prawidłowo?"""
		formatted_place = get_formatted_place('santiago', 'chile', '5000000')
		self.assertEqual(formatted_place, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
	unittest.main()