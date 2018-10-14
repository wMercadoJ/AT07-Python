from FranzSilva.practice_05.Shop import Shop


class Purchase:
    def __init__(self, shop):
        self.shop = shop
        self.items_purchase_amount = {}
        self.items_purchase_price = {}

    def add_purchase(self):
        item = input('Insert the item to purchasing:')
        quantity = int(input('Insert the quantity to purchasing(only numbers):'))
        while True:
            if self.shop.verify_availability(item, quantity):
                self.items_purchase_amount[item] = quantity
                self.items_purchase_price[item] = quantity * self.shop.get_price_item_in_shop(item)
                self.shop.update_amount_item(item, quantity)
                break
            else:
                print('The item is not available')
                break

    def print_items_purchased(self):
        print('********PURCHASED TOTAL********')
        for item in self.items_purchase_price:
            print('ITEM:', item)
            print('TOTAL_PRICE:', self.items_purchase_price[item])
            print('*******************************')

    def calculate_total_price( self ):
        '''Calculate the total price purchase'''
        total_price = 0
        for i in self.items_purchase_price:
            total_price += self.items_purchase_price[i]
        return total_price

    def balance( self, cash_paid ):
        total_price = int(self.calculate_total_price())
        if cash_paid < total_price:
            return "Cash paid not enough"
        return cash_paid - total_price

    def perform_purchase(self):
        while True:
            continue_purchase = input('Do you wanna buy?(yes/no)')
            if continue_purchase.lower() == 'yes':
                print(self.shop.show_items())
                self.add_purchase()
            else:
                self.print_items_purchased()
                print('The total price is:', self.calculate_total_price())
                print('The balance in your cart:', self.balance(100000))
                break


print('******************Welcome to Shopping Page******************')
store = Shop()
store.add_item('lapiz', 10, 5)
store.add_item('papel', 200, 9)
store.add_item('franz', 100, 7)
store.add_item('pan', 100, 1000)

shopping_cart = Purchase(store)
shopping_cart.perform_purchase()
