class Item:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity=quantity

    def set_price(self, price):
        """set item price"""
        self.price = price

    def set_quantity(self, quantity):
        """set item quantity"""
        self.quantity = quantity
