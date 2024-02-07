#!/usr/bin/python3
"""
Nothing imported here
"""


def append_write(filename="", text=""):
    """
    function that appends
    """
    with open(filename, mode='a', encoding='utf8') as file:
        n = file.write(text)
        return n
