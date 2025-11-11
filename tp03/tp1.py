class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)
"A class should have only one reason to change."

class OrderPrinter:
    def print_order(self, order):
        print("Order details:")
        for item in order.items:
            print(f"{item['name']}: ${item['price']}")


class OrderRepository:
    def save_to_db(self, order):
        print("Saving order to database...")

"Classes should be open for extension but closed for modification."
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

class Shape:
    def get_area(self):
        raise NotImplementedError("Must be implemented by subclass")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length


def print_area(shape):
    print(f"Area: {shape.get_area()}")

class Person:
    pass

class Employee(Person):
    def get_salary(self):
        pass
    def assign_task(self):
        pass

class Student(Person):
    def study(self):
        pass
class Printable:
    def print_document(self, document):
        pass


class Scannable:
    def scan_document(self, document):
        pass


class Faxable:
    def fax_document(self, document):
        pass


class BasicPrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")


class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")
class Teachable:
    def teach(self):
        pass


class Researchable:
    def research(self):
        pass


class Medicable:
    def practice_medicine(self):
        pass


class ProfessorResearcher(Teachable, Researchable):
    def teach(self):
        print("Teaching students...")

    def research(self):
        print("Conducting research...")


class FullTimeResearcher(Researchable):
    def research(self):
        print("Conducting full-time research...")


class ProfessorHospitalResearcher(Teachable, Researchable, Medicable):
    def teach(self):
        print("Teaching medical students...")

    def research(self):
        print("Publishing medical research...")

    def practice_medicine(self):
        print("Treating patients at the hospital...")
from abc import ABC, abstractmethod

# Abstraction
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Implementations
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushService(NotificationService):
    def send(self, message):
        print(f"Sending push notification: {message}")


# High-level module
class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def send(self, message):
        self.service.send(message)
if __name__ == '__main__':
    products = [
        {"name": "Fruit", "price": 50},
        {"name": "Vegetables", "price": 100},
        {"name": "Bread", "price": 20},
        {"name": "Meat", "price": 1000},
    ]

    my_order = Order(products)
    total = my_order.calculate_total()
    print("Total order:", total, "$")

    printer = OrderPrinter()
    repo = OrderRepository()

    printer.print_order(my_order)
    repo.save_to_db(my_order)
    price = 1000

    vip = VIPDiscount(price)
    print(f"VIP price: {vip.apply_discount()}")

    first_time = FirstTimeCustomerDiscount(price)
    print(f"First-time customer price: {first_time.apply_discount()}")

    regular = Discount(price)
    print(f"Regular price: {regular.apply_discount()}")
    rect = Rectangle(5, 10)
    square = Square(5)
    print_area(rect)
    print_area(square)
    basic = BasicPrinter()
    basic.print_document("Report.pdf")

    advanced = AdvancedPrinter()
    advanced.print_document("Thesis.pdf")
    advanced.scan_document("Thesis.pdf")
    advanced.fax_document("Thesis.pdf")
    email = EmailService()
    sms = SMSService()
    push = PushService()
    Notification(email).send("Hello via Email!")
    Notification(sms).send("Hello via SMS!")
    Notification(push).send("Hello via Push!")