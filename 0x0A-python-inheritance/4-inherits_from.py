#!/usr/bin/python3
"""
Nothing imported
"""


def inherits_from(obj, a_class):
    """
    Function to return an instance of object
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
