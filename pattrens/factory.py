#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

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

class Rectangle(Shape):
    def draw(self): 
        print("Rectangle.draw")
    def erase(self): 
        print("Rectangle.erase")

class Triangle(Shape):
    def draw(self): 
        print("Triangle.draw")
    def erase(self): 
        print("Triangle.erase")

if __name__ == "__main__":
    for type in ("Circle", "Square", "Rectangle", "Triangle"):
        if type == "Circle":
            shape = Circle()
        elif type == "Square":
            shape = Square()
        elif type == "Rectangle":
            shape = Rectangle()
        elif type == "Triangle":
            shape = Triangle()
        else:
            print("Bad shape creation: " + type)
            sys.exit()

        shape.draw()
        shape.erase()