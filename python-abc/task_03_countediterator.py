#!/usr/bin/python3

class CountedIterator:
    """extends the built-in iterator obtained from the iter function."""

    def __init__(self, iterable):
        """iterator and the counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return iterator"""
        return (self)

    def __next__(self):
        """Return next item and increment counter"""
        try:
            item = next(self.iterator)
            self.count += 1
            return (item)
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return current count of items iterated"""
        return (self.count)
