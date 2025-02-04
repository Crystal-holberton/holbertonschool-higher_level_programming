#!/usr/bin/python3
"""Create an abstract class named Animal using the ABC package."""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base for animal"""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sounds"""
        pass

class Dog(Animal):
    """Dog inherits from Animal"""

    def sound(self):
        """Return sound of Dog"""
        return ("Bark")

class Cat(Animal):
    """Cat inherits from Animal"""

    def sound(self):
        """Return sound of Cat"""
        return ("Meow")
