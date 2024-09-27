#!/usr/bin/python3
"""Squaring the matix"""


def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
