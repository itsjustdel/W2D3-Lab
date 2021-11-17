class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, customer, drink):
        # reduce money from customer
        customer.reduce_wallet(drink.price)         
        # add money to pub's till
        self.increase_till(drink.price)
        
