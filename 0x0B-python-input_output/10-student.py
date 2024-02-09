#!/usr/bin/python3
"""
NOthing imported
"""


class Student:
    """
    A class that represents a student
    """

    def __init__(self, first_name, last_name, age):
        """__init__ function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns representation of studen instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
