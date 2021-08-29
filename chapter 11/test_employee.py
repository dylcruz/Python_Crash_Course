import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the employee class"""
	def setUp(self):
		self.test_employee = Employee("Dylan", "Cruz", 45000)

	def test_give_default_raise(self):
		self.test_employee.give_raise()

	def test_give_custome_raise(self):
		self.test_employee.give_raise(10000)

unittest.main()