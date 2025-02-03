#!/usr/bin/python3
"""Class checking function"""


def is_same_class(obj, a_class):
    """
    Check if object is exactly an instance of the given class

    Args:
    obj (any): object to check
    a_class (type): class to match type of obj to
    Returns:
    If obj is exactly an instance of a_class - True
    Otherwise - Fasle
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
