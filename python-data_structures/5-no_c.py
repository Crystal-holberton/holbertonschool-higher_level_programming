#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for char in my_string:
        if char != "c" and char != "C":
            str += char
    return str
