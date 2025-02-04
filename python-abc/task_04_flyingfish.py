#!/usr/bin/python3

class Fish:
    """class for Fish"""

    def swim(self):
        """print fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """print habitat of fish"""
        print("The fish lives in water")


class Bird:
    """class for bird"""

    def fly(self):
        """print bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """print habitat of bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class for flying fish, inheriting from Fish and Bird"""

    def fly(self):
        """print flying fish is soaring"""
        print("The flying fish is soaring!")

    def swim(self):
        """print flying fish is swimming"""
        print("The flying fish is swimming!")

    def habitat(self):
        """print habitat of flying fish"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())
