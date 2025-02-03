#!/usr/bin/python3
"""inherited class checking function"""


def inherits_from(obj, a_class):
    """
    Checks if object is an inherited instance of class

    Args:
    obj (any): object to check
    a_class (type): class to match type of object to
    Returns:
    True: if obj is an inherited instance of a_class
    False: Otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
