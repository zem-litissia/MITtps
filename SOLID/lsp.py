class Rectangle:
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):  
    def set_width(self, width):
        self.width = width
        self.height = width 

    def set_height(self, height):
        self.height = height
        self.width = height  


def print_area(rectangle):
   
    print(f"Area: {rectangle.get_area()}")


if __name__ == '__main__':
   
    rect = Rectangle()
    rect.set_width(5)
    rect.set_height(10)

    square = Square()
    square.set_width(5)
    square.set_height(10)

    print_area(rect)    
    print_area(square)  
