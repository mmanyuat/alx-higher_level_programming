#!/usr/bin/python3
"""NO imported Module"""


class Rectangle:
    """A class that defines rectangle"""
    def __init__(self, width=0, height=0):
        """A constructor that instantiate the object"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter to retirve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A func to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """"A getter to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
