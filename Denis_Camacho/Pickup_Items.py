from Denis_Camacho.logger import logger


class Pickup_Items:
    def __init__(self, item, price, amount):
        self.item = item
        self.price = price
        self.amount = amount
        self.items = []
        self.items.append([item, price, amount])

    def show_items(self):
        logger.info("into a show_items")
        return self.items

    def add_item(self, new_item, price, amount):
        logger.info("into a add_item")
        verify_item = False
        for i in range(0, len(self.items)):
            if self.items[i][0] == new_item:
                logger.debug("the item not is new :" + self.items[i][0])
                verify_item = True
                self.items[i][1] = price
                self.items[i][2] += amount
                break
        if not verify_item:
            logger.debug("the item is new :" + new_item)
            self.items.append([new_item, price, amount])
