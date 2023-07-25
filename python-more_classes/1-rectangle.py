#!/usr/bin/python3
"""A class that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):

    """Initialize a new rectangle


    Args:
    width (int): The width of the new rectangle
    height (int): The height of the new rectangle
    """
    
    self.width = width
    self.height = height

    @property
    def width(self):
        """property (get&set) for the current width of rectangle"""
        return (self.width)

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """property (get&set) for the current width of rectangle"""
        return (self.height)

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
