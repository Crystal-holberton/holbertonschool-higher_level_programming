#!/usr/bin/python3
"""Definess a rectangle"""


class Rectangle:
    """
    Represents a rectangle
    Attributes:
    number_of_instances (int): number of rectangle instances
    print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise new rectangle
        Args:
        width (int): width of new rectangle
        height (int): height of new rectanlge
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join([
            str(self.print_symbol) * self.__width for _ in range(self.__height)
            ]))

    def __repr__(self):
        """Return the string representation of a rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Deletion message for every deleted rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Retrun biggest rectangle based on area
        Args:
        rect_1 (Rectangle): first rectangle
        rect_2 (Rectangle): second rectangle
        Raises:
        TypeError: if either is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
