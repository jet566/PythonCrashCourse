from employee import Employee
import unittest

class EmployeeTestCase(unittest.TestCase):
	"""Test dla programu employee.py"""
	def setUp(self):
		"""Utworzenie profilu pracownika do użycia we wszystkich metodach testowych"""
		self.my_employee = Employee('Jan', 'Kowalski', 50_000)

	def test_give_default_raise(self):
		"""Testuje czy pracownik dostał podwyżkę o kwotę domyślną - 5000 zł"""
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary , 55_000)

	def test_give_custom_raise(self):
		"""Testuje czy pracownik dostał podwyżkę"""
		self.my_employee.give_raise(10_000)
		self.assertEqual(self.my_employee.salary, 60_000)

if __name__ == '__main__':
	unittest.main()