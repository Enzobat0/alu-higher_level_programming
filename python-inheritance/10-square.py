#!/usr/bin/python3
'''creates a subclass Square from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size

        def area(self):
        '''function to return the area of a rectangle'''
        r_area = self.__width * self.__height
        return r_area
