import unittest
from city_functions import city_country
class cityTestCase(unittest.TestCase):
	def test_city_country(self):
		mm_home=city_country('jinhua','china','500000')
		self.assertEqual(mm_home,'Jinhua,China -population 500000')
	def test_city_country_puplation(self):
		mm_home=city_country('jinhua','china')
		self.assertEqual(mm_home,'Jinhua,China')
		
unittest.main()
