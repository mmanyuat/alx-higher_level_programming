#!/usr/bin/python3
"""
No module imported
"""


def write_file(filename="", text=""):
    """
    Function that write to text
    and returns the number of characters
    """
    with open(filename, mode='w', encoding='UTF8') as file:
        n = file.write(text)
        return n
