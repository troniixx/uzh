from Item import Item
from Order import Order

__author__ = "Mert Erol"

class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__cash = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        if len(order_list) == 0:
            return "No order yet"
        else: return order_list

    def set_order(self, item_list): #fix this using o
        o = Order(item_list)
        
        for item in item_list:
            if item in self.__menu_list:
                self.__cash.append(item.get_item_price())
        #print(self.__cash)

    def get_revenue(self):
        revenue = 0
        for num in self.__cash:
            revenue += num
        
        return revenue

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]
    # Create order list
    order_list = [steak, steak, salad, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
