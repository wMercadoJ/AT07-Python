class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount -= amount


class PickupItem:
    list_item = []

    def __init__(self):
        self.amount_item_pickup = 0

    def add_item(self, item):
        self.list_item.append(item)

    def buy_item(self, name_item, amount):
        print(self.list_item)
        for item in self.list_item:
            if item.get_name() == name_item:
                item.set_amount(amount)
            print("product " + item.get_name() + " price of product " + str(item.get_price() * amount))
            print("quantity " + str(item.get_amount()))
            break


def buy_product():
    name_item_buy = input("choose product")
    amount_item_buy = int(input("quantity of product"))
    pickup_item = PickupItem()
    pickup_item.buy_item(name_item_buy, amount_item_buy)


orange = Item("orange", 2, 20)
apple = Item("apple", 3, 10)
watermelon = Item("watermelon", 10, 6)
marker = PickupItem()
marker.add_item(orange)
marker.add_item(apple)
marker.add_item(watermelon)
buy_product()
