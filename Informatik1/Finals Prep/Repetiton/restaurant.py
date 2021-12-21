class Item:
    # Set Item ID, Type and Name in initialization
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Return Item Name
    def get_item_name(self):
        return self.__name

    # Return Item Price
    def get_item_price(self):
        return self.__price

    def __repr__(self):
        return self.__name


class Order:
    def __init__(self, item_list):
        self.__item_list = self.__get_item_list(item_list)
        self.__bill_amount = self.__calculate_bill_amount(item_list)

    def __get_item_list(self, item_list):
        d = {}
        for item in item_list:
            try:
                d[item] += 1
            except KeyError:
                d[item] = 1
        return d

    def get_bill_amount(self):
        return self.__bill_amount

    def __calculate_bill_amount(self, item_list):
        bill_amount = 0
        for item in item_list:
            bill_amount = item.get_item_price() + bill_amount
        return bill_amount

    def __repr__(self):
        return "Order Items : {}, Order Bill Amount : {} ".format(self.__item_list, self.__bill_amount)



class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.restaurant_name = restaurant_name
        self.menu_list = menu_list
        self.order_list = []

    def get_restaurant_name(self):
        return self.restaurant_name

    def get_menu_list(self):
        return self.menu_list

    def get_order_list(self):
        if len(self.order_list) == 0:
            return "No orders yet"
        return self.order_list

    def set_order(self, item_list):
        actual = []
        for item in item_list:
            if item in self.menu_list:
                actual.append(item)
        
        if len(actual) != 0:
            o = Order(actual)
            self.order_list.append(o)

    def get_revenue(self):
        rev = 0
        for order in self.order_list:
            rev += order.get_bill_amount()
        
        return rev


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
