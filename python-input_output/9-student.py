#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Represents Student"""

    def __init__(self, first_name, last_name, age):
        """retrieves a dictionary representation of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of a Student"""
        return self.__dict__
