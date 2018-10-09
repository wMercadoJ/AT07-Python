class Pickup_Items:
    def __init__(self, item, price, amount):
        self.item = item
        self.price = price
        self.amount = amount
        self.items = []
        self.items.append([item, price, amount])

    def show_items(self):
        return self.items

    def add_item(self, new_item, price, amount):
        verify_item = False
        for i in range(0, len(self.items)):
            if self.items[i][0] == new_item:
                verify_item = True
                self.items[i][1] = price
                self.items[i][2] += amount
                break
        if not verify_item:
            self.items.append([new_item, price, amount])

    def buy_item(self, item, amount):
        for i in range(0, len(self.items)):
            if self.items[i][0] == item:
                if amount <= self.items[i][2]:
                    self.items[i][2] -= amount
                    return "buy successfully the price is:" + str(self.items[i][1] * amount)
        return "no found the item"


pickup_items = Pickup_Items("samsung j7", 1800, 10)
print(pickup_items.show_items())
pickup_items.add_item("samsung j7", 1750, 15)
pickup_items.add_item("huawei p20", 1600, 20)
print(pickup_items.show_items())
print(pickup_items.buy_item("huawei p20", 10))
print(pickup_items.show_items())
