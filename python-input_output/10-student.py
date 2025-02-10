#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Represents Student"""

    def __init__(self, first_name, last_name, age):
        """retrieves a dictionary representation of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of a Student"""
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self,k)}
        return self.__dict__
