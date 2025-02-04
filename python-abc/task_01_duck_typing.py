#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """calculate area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """calculate perimeter of shape"""
        pass

class Circle(Shape):
    """Circle inherits from Shape"""

    def __init__(self, radius):
        """Circle with radius"""
        self.__radius = abs(radius)

    def area(self):
        """calculate area of circle"""
        return (math.pi * (self.__radius ** 2))

    def perimeter(self):
        """calculate perimeter of circle"""
        return (2 * math.pi * self.__radius)

class Rectangle(Shape):
    """Rectangle inherits from Shape"""

    def __init__(self, width, height):
        """Rectangle with width and height"""
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate perimeter of Rectangle"""
        return (2 * (self.__width + self.__height))

def shape_info(shape):
    """Print area and perimeter of Shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Testing
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
