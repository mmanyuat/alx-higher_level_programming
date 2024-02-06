#!/usr/bin/python3
"""
Nothing imported here
"""


class MyList(list):
    """
    A subclass inherited from list
    """

    def print_sorted(self):
        """
        prints the list in the sorted or ascending order
        """

        print(sorted(self))
