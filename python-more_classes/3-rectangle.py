#!/usr/bin/python3
"""Definess a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialise new rectangle
        Args:
        width (int): width of new rectangle
        height (int): height of new rectanlge
        """
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
        return ("\n".join(["#" * self.__width for _ in range(self.__height)]))
