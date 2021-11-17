import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John" , 50.45)

    def test_name(self):
        self.assertEqual("John" , self.customer.name)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(2)
        self.assertEqual(48.45, self.customer.wallet)