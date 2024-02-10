#!/usr/bin/python3
""" NOthing imported """


def add_integer(a, b=98):
    """
    A function that adds two integers
    Adds 2 integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98 if not provided.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

        """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
