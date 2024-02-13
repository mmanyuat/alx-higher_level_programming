#!/usr/bin/python3
"""Module imported from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Function that initiliazes square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of a sqaure"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getters for size"""
        return self.width

    @size.setter
    def size(self, value):
        """ Setters for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attribute of the square"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
