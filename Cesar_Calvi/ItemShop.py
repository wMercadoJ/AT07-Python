itemsToShop = [
    ("Play Station 3", 65.0, 50),
    ("Leather jacket", 32.5, 50),
    ("Harry potter and the Philosopher's Stone", 10.0, 50),
    ("Harry Potter ", 10.0, 50)
]


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class ItemShop:
    def __init__(self):
        self.items = []
        self.totalPrice = 0.0
        self.ITEM = 0
        self.PRICE = 1
        self.AMOUNT = 2

    def ask_for_item(self, item):
        for i in range(0, len(itemsToShop)):
            if itemsToShop[i][self.ITEM].lower() == item.lower():
                return "OK", i
        return "Does not exist", None

    def buy_item(self, item, amount):
        res, ind = self.askForItem(item)
        if res == "OK":
            prod = itemsToShop[ind]
            fullPrice = prod[self.PRICE] * amount
            resAmount = prod[self.AMOUNT] - amount
            if resAmount < 0:
                print ("PURCHASE CANCELED, THERE ARE NOT SUFFICIENT UNITS IN STOCK")
            else:
                itemsToShop[ind] = (prod[self.ITEM], prod[self.PRICE], resAmount)
                self.items.append((prod[self.ITEM], fullPrice, amount))
                self.totalPrice = self.totalPrice + fullPrice
                print ""
                print "BUYED PURCHASE: item = ", prod[self.ITEM], " price = ", fullPrice, " Amount = ", amount
                print "      Total price : ", self.totalPrice, "  REMAINING AMOUNT IN STOCK : ", resAmount
                print ""
        else:
            print "THE PRODUCT DOES NOT EXIST"

    def run_shop(self):
        print "-- Welcome!"
        op = "1"
        while op != "0":
            print ""
            print "MENU"
            print "1) Buy Item"
            print "0) Exit"
            print "2) See items list"
            op = str(raw_input())
            if op == "1":
                print ""
                op3 = "y"
                while op3 != "n":
                    print "ITEMS:"
                    for i in range(0, len(itemsToShop)):
                        print i, ") ", itemsToShop[i][self.ITEM]
                    op2 = str(raw_input())
                    if is_number(op2) is True and int(op2) <= len(itemsToShop) and not int(op2) < 0:
                        print "Enter amount: "
                        cant = int(raw_input())
                        it = itemsToShop[int(op2)][self.ITEM]
                        print ""
                        print "Item: ", it
                        print "Amount: ", cant
                        self.buyItem(it, cant)
                    print ""
                    print "WISH TO MAKE ANOTHER PURCHASE ? Y = Yes, N = No"
                    aux = str(raw_input())
                    op3 = aux.lower()
                self.items = []
                self.totalPrice = 0.0
            if op == "2":
                for i in range(0, len(itemsToShop)):
                    print i, ") ", itemsToShop[i][self.ITEM]
                    print "Amount   ----", itemsToShop[i][self.AMOUNT]
                    print "Price    ----", itemsToShop[i][self.PRICE]
                    print " "

        print "FIN"


if __name__ == '__main__':
    shop = ItemShop()
    shop.runShop()
