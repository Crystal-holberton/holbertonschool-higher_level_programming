#!/usr/bin/python3
"""class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGoemetry"""

    def __init__(self, width, height):
        """
        Initialise a new rectangle
        
        Args:
        width (int): width of new Rectangle
        height (int): height of new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
