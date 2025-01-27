#!/usr/bin/python3
"""An empty class that defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """
        Create new square
        Args:
        size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
