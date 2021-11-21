import item
import order

__author__ = "Mert Erol"

class Restaurant:

    global cash
    cash = []

    def __init__(self, restaurant_name, menu_list):
        self.restaurant_name = restaurant_name
        self.menu_list = menu_list

    def get_restaurant_name(self):
        return self.restaurant_name

    def get_menu_list(self):
        return self.menu_list

    def get_order_list(self):
        if len(order_list) == 0:
            return "No order yet"
        else: return order_list

    def set_order(self, item_list):
        o = Order()
        o.__get_item_list(item_list)
        o.get_bill_amount(item_list)
        x = o.__calculate_bill_amount(item_list)

        cash.append(x)

    def get_revenue(self):
        revenue = 0
        for num in cash:
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
