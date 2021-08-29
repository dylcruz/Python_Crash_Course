import unittest
from city_functions import get_formatted_city

class NameTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_name = get_formatted_city('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')

	def test_city_country_pop(self):
		formatted_name = get_formatted_city('santiago', 'chile', 5000000)
		self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000000')

unittest.main()