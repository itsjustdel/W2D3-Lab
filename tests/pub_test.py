import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Beer", 5.00, 5)
        self.customer1 = Customer("Jimmy", 100.00, 70)
        self.customer2 = Customer("Calum", 10, 16)
        self.customer3 = Customer("Adam", 0, 23)

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

    def test_check_age(self):
        self.assertEqual(self.pub.check_age(self.customer1), True)
        self.assertEqual(self.pub.check_age(self.customer2), False)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer1, self.drink1)
        self.assertEqual(self.pub.till, 105.00)
        self.assertEqual(self.customer1.wallet, 95.00)

    def test_sell_drink_result(self):
        self.assertEqual(True, self.pub.sell_drink(self.customer1, self.drink1))
        self.assertEqual(False, self.pub.sell_drink(self.customer2, self.drink1))
        self.assertEqual(False, self.pub.sell_drink(self.customer3, self.drink1))

    def test_alcohol_level(self):
        self.pub.sell_drink(self.customer1, self.drink1)
        self.assertEqual(self.customer1.drunkenness, 5)

    def test_max_drunkenness(self):
        for i in range(4):
            self.pub.sell_drink(self.customer1, self.drink1)
        self.assertEqual(False, self.pub.sell_drink(self.customer1, self.drink1))
