#!/usr/bin/python3
"""
NO modules imported
"""


class Rectangle:
    """
    A class that represents a rctangle

    Attributes:
    width, hights

    Methods:
    width, heights, area, paremeter, area
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (("#" * self.width + "\n") * self.height).strip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    if __name__ == "__main__":
        my_rectangle = Rectangle(2, 4)
        print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")
        del my_rectangle

        try:
            print(my_rectangle)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
