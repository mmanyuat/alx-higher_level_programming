#!/usr/bin/python3
"""Nothing imported for this class"""


class Rectangle:
    """A Rectangle blueprint"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """THe constructor"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """A getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that returns the area"""
        return (self.width * self.height)

    def perimeter(self):
        """Method that computes the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """Print the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            row = str(self.print_symbol) * self.width
            return "\n".join([row] * self.height)

    def __repr__(self):
        """Returns the string representation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deleting an instance of the object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
