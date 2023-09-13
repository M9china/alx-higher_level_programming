#!/usr/bin/python3
"""holds the MyList class"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
