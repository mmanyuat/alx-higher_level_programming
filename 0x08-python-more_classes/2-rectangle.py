#!/usr/bin/python3
"""
A class with no imported module
"""


class Rectangle:
    """
    A class that represents a Rctangle

    Attributes:
    parameters:width, heights

    methods: width, height, area and parameters
    """

    def __init__(self, width=0, height=0):
        """A constructor that instanstiate the task"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter"""
        return 2*(self.__width + self.__height)
