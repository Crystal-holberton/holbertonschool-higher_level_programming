#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initialises the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
