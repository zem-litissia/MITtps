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

if __name__ == "__main__":
    for type in ("Circle", "Square", "Circle", "Square"):
        if type == "Circle":
            shape = Circle()
        elif type == "Square":
            shape = Square()
        else:
            print("Bad shape creation: " + type)
            sys.exit()

        shape.draw()
        shape.erase()
