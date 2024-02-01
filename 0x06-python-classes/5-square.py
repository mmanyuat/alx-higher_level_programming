#!/usr/bin/python3
"""
No imported module
"""


class Square:
    """
    A class that represents a Square

    Attributres:
    __size
    Methods:
    size, __init__ , area, my_print
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
        return size * size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
