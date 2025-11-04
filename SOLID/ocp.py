
class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self):
        return self.price



class VIPDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.8  # 20% discount



class FirstTimeCustomerDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.9  # 10% discount

# main after OCP
if __name__ == '__main__':
    price = 1000

    vip = VIPDiscount(price)
    print(f"VIP customer: Old price = {price}, New price = {vip.apply_discount()}")

    first_time = FirstTimeCustomerDiscount(price)
    print(f"First-time customer: Old price = {price}, New price = {first_time.apply_discount()}")
