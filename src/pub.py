class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till

        ##
        self.drinks = {}
        self.max_drunkenness = 20

    def increase_till(self, amount):
        self.till += amount

    def add_drink(self, drink, stock_level):
        self.drinks[drink] = stock_level

    def check_age(self, customer):
        return customer.age >= 18

    def sell_drink(self, customer, drink):
        # check customer at least 18
        if self.check_age(customer) and customer.wallet >= drink.price and customer.drunkenness < self.max_drunkenness:
            # reduce money from customer
            customer.reduce_wallet(drink.price)         
            # add money to pub's till
            self.increase_till(drink.price)

            customer.drunkenness += drink.alcohol_level
            return True
        else:
            return False

    def sell_food(self, customer, food):
        # check customer has money for food!
        if customer.wallet >= food.price:            
            # make customer feel better            
            customer.drunkenness -= food.rejuvenation_level
            if customer.drunkenness < 0:
                customer.drunkenness = 0

            return True
        else:
            return False

    def stock_value(self):
        total_value = 0
        for drink in self.drinks:
            total_value += self.drinks[drink] * drink.value

        return total_value


        
