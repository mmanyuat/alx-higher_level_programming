#!/usr/bin/python3
"""
NO imported module
"""


class Square:
    """
    A class that reprsents a square

    Attributes:
    __size
    Methods:
    size, area, init
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size * self.size
