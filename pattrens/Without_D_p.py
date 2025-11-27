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

class Rectangle:
    def draw(self): print("Rectangle.draw")
    def erase(self): print("Rectangle.erase")

class Triangle:
    def draw(self): print("Triangle.draw")
    def erase(self): print("Triangle.erase")
    


class ShapeFactory_SCT:
    @staticmethod
    def createShape(type):
        if type == "Circle": 
            return Circle()
        elif type == "Square": 
            return Square()
        elif type == "Triangle": 
            return Triangle()
        else:
            print("Bad shape creation: " + type)
            sys.exit()


class ShapeFactory_SCR:
    @staticmethod
    def createShape(type):
        if type == "Circle": 
            return Circle()
        elif type == "Square": 
            return Square()
        elif type == "Rectangle": 
            return Rectangle()
        else:
            print("Bad shape creation: " + type)
            sys.exit()


if __name__ == "__main__":
    print("Testing SCT Factory:")
    for type in ("Circle", "Square", "Triangle"):
        shape = ShapeFactory_SCT.createShape(type)
        shape.draw()
        shape.erase()
    
    print("\nTesting SCR Factory:")
    for type in ("Circle", "Square", "Rectangle"):
        shape = ShapeFactory_SCR.createShape(type)
        shape.draw()
        shape.erase()