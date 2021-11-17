import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Beer", 5.00)
        self.customer1 = Customer("Jimmy", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        # Arrange
        # Act
        self.pub.increase_till(2.50)
        # Assert
        expected  = 102.5
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_add_drink(self):        
        # Act
        self.pub.add_drink(self.drink1)
        # Assert
        self.assertEqual(1, len(self.pub.drinks))

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer1, self.drink1)
        self.assertEqual(self.pub.till, 105.00)
        self.assertEqual(self.customer1.wallet, 95.00)


    

    

