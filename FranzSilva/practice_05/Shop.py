from FranzSilva.practice_05.Item import Item


class Shop:

    def __init__(self):
        self.list_items = []

    def add_item(self, name_item, price, quantity):
        self.list_items.append(Item(name_item, price, quantity))

    def verify_availability(self, name_item, quantity):
        for item in self.list_items:
            if name_item == item.name:
                return 0 < quantity < item.quantity + 1
        return False

    def get_price_item_in_shop(self, name_item):
        for item in self.list_items:
            if name_item == item.name:
                return item.price

    def update_amount_item(self, name_item, quantity):
        for item in self.list_items:
            if name_item == item.name:
                item.quantity -= quantity

    def show_items( self):
        print("Enable Items: ")
        print("{0}{1}{0}{2}".format("|", "ITEMS", "QUANTITY"))
        for items in self.list_items:
            print("{0}{1}{0}{2}".format("|", items.name, items.quantity))
