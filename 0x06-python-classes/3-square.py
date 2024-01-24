#!/usr/bin/python3
"""
No module used here
"""


class Square:
    """
    A class representing square

    Attributes:
    __size(int): use size which is optional
    """
    def __init__(self, size=0):
        """
        initialse a square class with size
        parameters:
        size(int, optional):takes size with default value of 0
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less then 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """
        instance that returns square area
        """
        return self.__size ** 2
