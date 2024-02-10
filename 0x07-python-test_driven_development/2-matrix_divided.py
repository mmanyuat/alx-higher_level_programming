#!/usr/bin/python3
""" Nothing imported """


def matrix_divided(matrix, div):
    """
    A function that divides all the elements of a matrix

    attributes:
    matrix - the matrix provided
    div - the number to divide the element of the matrix

    raise TypeError - matrix must be a matrix (list of lists) of
    raise ZeroDivisionError - division by zero
    TypeError - Each row of the matrix must have the same size
    """

    if not isinstance(matrix, list) or not all
    (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix(
                list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
