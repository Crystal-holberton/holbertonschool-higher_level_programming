#!/usr/bin/python3

class SwimMixin:
    """Mixin class adding swimming ability"""

    def swim(self):
        """Prints creature can swim"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class adding flying ability"""

    def fly(self):
        """Prints creature can fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon, inherits swim and fly"""

    def roar(self):
        """Print dragon roars"""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
