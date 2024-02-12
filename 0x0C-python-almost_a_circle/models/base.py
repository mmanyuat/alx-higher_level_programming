#!/usr/bin/python3
"""
NOthing imported
"""


class Base:
    """
    Class that represents base class
    private attributes: __nb_objects = 0
    class constructor: def __init__(self, id=None):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
