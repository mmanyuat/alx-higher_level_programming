#!/usr/bin/python3
"""
Module to define the class square
"""


class Square:
    """
    A class that represnts an instance with size 0

    Attributes:
    __size(int):private attribute of size int

    """
    def __init__(self, size=0):
        """
        intilizes class parameter with optional size
        Parameters:
        size(int, optional): option parameters that defaults to 0
        Raise:
        TypeError: if not an integer
        ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
