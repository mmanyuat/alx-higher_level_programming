#!/usr/bin/python3
"""
No imported module
"""


class Square:
    """
    A class that represents a Square

    Attributres:
    __size
    Methods:
    size, __init__ , area, my_print
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        result = ""
        if self.size == 0:
            result += "\n"
        else:
            for _ in range(self.position[1]):
                result += "\n"
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        return result.strip('\n')
    
if __name__ == "__main__":
    my_sqaure = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
