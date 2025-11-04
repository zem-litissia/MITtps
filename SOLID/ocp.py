class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def apply_discount(self):
        if self.customer == 'VIP':
            return self.price * 0.8  # 20% discount
        return self.price


if __name__ == '__main__':
    price = 1000
    customer = "VIP"
    mydiscount = Discount(customer, price)
    newprice = mydiscount.apply_discount()
    print(f"Old Price: {price} for {customer}, New price {newprice}")

    price = 1000
    customer = "regular"
    # discount of 5%
    mydiscount2 = Discount(customer, price)
    newprice2 = mydiscount2.apply_discount()
    print(f"Old Price: {price} for {customer}, New price {newprice2}")
