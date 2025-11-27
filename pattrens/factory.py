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



class ShapeFactory:
    @staticmethod
    def createShape(type):
        if type == "Circle": 
            return Circle()
        elif type == "Square": 
            return Square()

        else:
            print("Bad shape creation: " + type)
            sys.exit()

if __name__ == "__main__":
    for type in ("Circle", "Square", "Circle", "Square"):
        shape = ShapeFactory.createShape(type)
        shape.draw()
        shape.erase()