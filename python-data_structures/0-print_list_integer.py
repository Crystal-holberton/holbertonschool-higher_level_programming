#!/usr/bin/python3
#0-print_list_integer.py
#Crystal Carroll <9188@holbertonstudents.com>

def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for value in my_list:
        print("{:d}".format(value))
