import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Wine", 6.50)
    
    def test_name(self):
        self.assertEqual("Wine", self.drink1.name)

    def test_price(self):
        self.assertEqual(6.50, self.drink1.price)
        

    