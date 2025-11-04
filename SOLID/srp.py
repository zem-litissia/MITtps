class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

    def print_order(self):
        print("Order details:")
        for item in self.items:
            print(f"{item['name']}: ${item['price']}")

    def save_to_db(self):
        print("Saving order to database...")


if __name__ == '__main__':
    products = [
        {"name": "fruit", "price": 50},
        {"name": "vegetables", "price": 100},
        {"name": "Bread", "price": 20},
        {"name": "Meat", "price": 1000},
    ]

    my_order = Order(products)
    total = my_order.calculate_total()
    print("Total order:", total, "$")
    my_order.print_order()
    my_order.save_to_db()
