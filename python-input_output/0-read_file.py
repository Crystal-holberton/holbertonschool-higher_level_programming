#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """reads text file (UTF8) and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
