#!/usr/bin/python3

class VerboseList(list):
    """list that prints notifications on modifications"""

    def append(self, item):
        """Add an item"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove the first occurance"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index = -1):
        """Remove and return item at index"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return (item)
