from Denis_Camacho.pickup_items import Pickup_Items, logger


class Buy_item(Pickup_Items):
    def __init__(self, item, price, amount):
        Pickup_Items.__init__(self, item, price, amount)
        self.items_add = []

    def buy_item(self):
        logger.info("into to buy_item")
        buy_item = input("into the item please eg. 'pencil' ")
        buy_amount = int(input("into the amount please eg. 10 "))

        for i in range(0, len(self.items)):
            if self.items[i][0] == buy_item:
                logger.debug("verify the buy_item: " + buy_item)
                if buy_amount <= self.items[i][2]:
                    logger.debug("verify the buy_amount: " + str(buy_amount))
                    self.items_add.append([buy_item, self.items[i][1], buy_amount])
                    self.items[i][2] -= buy_amount
                    return "buy successfully the price is:" + str(self.items[i][1] * buy_amount)
        return "no found the item"


buy_items = Buy_item("samsung j7", 1600, 10)
buy_items.add_item("samsung j7", 1600, 20)
buy_items.add_item("huawei p20", 1700, 30)
print(buy_items.buy_item())
print(buy_items.items_add)
print(buy_items.items)
