#!/usr/bin/python3
"""A models that inherits base from base"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle that inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ function which intilizeses the class
        the attributes
        width - of the class
        height - of the class
        x - value
        y - value
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        function that gets the widths and returns it privately
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        function that sets the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        function that sets height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        function that sets height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        function that gets a value
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        function that sets a value
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        function that sets a value y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        function that gets value
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        function that computes area
        """

        return self.__width * self.__height

    def display(self):
        """
        function that display a #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ String representation of Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ function update """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A represanttion of rectangle as dictionary"""
        return{
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
