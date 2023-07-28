#!/usr/bin/python3
"""a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """A class"""

    def area(self):
        """A function that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that checks if its an int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
