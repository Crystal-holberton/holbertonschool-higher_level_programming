#!/usr/bin/python3
"""Define a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """size (int) of new Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of Square"""
        return (self.__size * self.__size)

    def __str__(self):
        """Description of Square"""
        return (f"[Square] {self.__size}/{self.__size}")
