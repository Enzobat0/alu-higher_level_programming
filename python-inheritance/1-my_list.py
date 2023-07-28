#!/usr/bin/python3
"""A class MyList that inherits from List"""


class MyList(list):
    """A class named MyList"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
