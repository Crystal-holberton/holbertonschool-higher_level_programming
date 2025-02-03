#!/usr/bin/python3
"""Create empty class 'BaseGeometry'"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer

        Args:
        name (str): name of parameter
        value (int): parameter to validate
        Raises:
        TypeError: if value is not an integer
        ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
