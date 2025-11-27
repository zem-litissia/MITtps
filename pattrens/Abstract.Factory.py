import sys
from abc import ABC, abstractmethod
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Shape:
    def draw(self): pass
    def erase(self): pass

class Circle(Shape):
    def draw(self): 
        print("Circle.draw")
    def erase(self): 
        print("Circle.erase")

class Square(Shape):
    def draw(self): 
        print("Square.draw")
    def erase(self): 
        print("Square.erase")

class Circle2D(Circle):
    def draw(self):
        print("Circle.draw2D")
    def erase(self):
        print("Circle.erase2D")

class Square2D(Square):
    def draw(self):
        print("Square.draw2D")
    def erase(self):
        print("Square.erase2D")

class Circle3D(Circle):
    def draw(self):
        print("Circle.draw3D")
    def erase(self):
        print("Circle.erase3D")

class Square3D(Square):
    def draw(self):
        print("Square.draw3D")
    def erase(self):
        print("Square.erase3D")

class ShapeFactory:
    @staticmethod
    def createShape(type):pass


class ShapeFactory2D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type.lower() == "circle":
            return Circle2D()
        elif type.lower() == "square":
            return Square2D()
        else:
            return None

class ShapeFactory3D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type.lower() == "circle":
            return Circle3D()
        elif type.lower() == "square":
            return Square3D()
        else:
            return None

if __name__ == "__main__":
    print("2D Shapes:")
    for type in ("Circle", "Square", "Circle", "Square"):
        shape = ShapeFactory2D.createShape(type)
        shape.draw()
        shape.erase()

    print("\n3D Shapes:")
    for type in ("Circle", "Square", "Circle", "Square"):
        shape = ShapeFactory3D.createShape(type)
        shape.draw()
        shape.erase()
