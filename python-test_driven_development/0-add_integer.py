#!/usr/bin/python3
"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    a and b must be first casted to integers if they are float
    raise a TypeError exception if a and b  not int or float"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
