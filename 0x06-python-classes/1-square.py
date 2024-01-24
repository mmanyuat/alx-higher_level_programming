#!/usr/bin/python3
"""
module for definining the sqaure class
"""


class Square:
    """
    A class that defines asquare

    Attributes:
    __size(int):private attribute representing the size of the size
    """
    def __init__(self, size):
        """
        initilizes the sqaure with an instance size
        parameters:
        __size(int):the size of the sqaure
        """
        self.__size = size
