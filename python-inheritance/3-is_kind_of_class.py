#!/usr/bin/python3
"""Defines a class and inherited class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance or
    inherited instance of a class

    Args:
    obj (any): object to check
    a_class (type): class to match the type of obj to
    Returns:
    True: if obj is instance or inherited instance of a_class
    False: Otherwise
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
