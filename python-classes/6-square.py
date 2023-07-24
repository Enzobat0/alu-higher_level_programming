#!/usr/bin/python3
"""A class that defines a square by: (5-square.py)"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property(get&set) for the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property(get&set for the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all( isinstance(i, int) for i in value) and all(i >= 0 for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the current area of the square."""
        return (self.__size**2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__postion[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], ends="")
                print ("#" * self.__size)
