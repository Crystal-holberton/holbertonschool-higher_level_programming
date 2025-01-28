#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Make a new square
        Args:
        size (int): size of new square
        position (int, int): position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get/set current position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set value of position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

