#!/usr/bin/python3
"""
Nothing imported
"""


def read_file(filename=""):
    """
    function that opens a file
    """

    with open(filename, encoding='UTF8') as f:
        f_contents = f.read()
        print(f_contents, end='')
        if __name__ == "__main__":
            read_file("my_file_0.txt")
