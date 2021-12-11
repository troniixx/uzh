from Item import Item
from Order import Order

__author__ = "Mert Erol"

class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__order_list = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        if len(self.__order_list)==0:
            return "No order yet"
        return self.__order_list

    def set_order(self, item_list):
        actual_order_list = []
        for i in item_list:
            if i in self.__menu_list:
                actual_order_list.append(i)
        if not len(actual_order_list) == 0:
            o = Order(actual_order_list)
            self.__order_list.append(o)

    def get_revenue(self):
        total_rev = 0
        for o in self.__order_list:
            total_rev += o.get_bill_amount()
        return total_rev


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    hamburger = Item("Hamburger", 20)
    # Create menu list
    menu_list = [hamburger, pizza, fish, salad]
    # Create order list
    order_list = [salad, steak, fish, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("SzeneMene", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
    print(restaurant.get_restaurant_name())
    print(restaurant.get_menu_list())
    print(restaurant.get_order_list())