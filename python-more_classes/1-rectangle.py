#!/usr/bin/python3
"""A class that defines a rectangle by: (0-rectangle.py)"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width, height):

    """Initialize a new rectangle


    Args:
    width (int): The width of the new rectangle
    height (int): The height of the new rectangle
    """
    
    self.width = width
    self.height = height

    @property
