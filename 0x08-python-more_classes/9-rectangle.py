#!/usr/bin/python3
"""Nothing imported"""


class Rectangle:
    """"A class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """"Constructor of the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle"""
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
        """Getter method to retrieve the height"""
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
        """Calculates the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (2 * (self.width + self.height))

    def __str__(self):
        """Renders the string representation of the instant"""
        if self.width == 0 or self.height == 0:
            return ""
        row = (str(Rectangle.print_symbol) * self.width)
        return "\n".join([row] * self.height)

    def __repr__(self):
        """Gets the object representation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes an instant of a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_2
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Renders a Square"""
        return cls(size, size)
