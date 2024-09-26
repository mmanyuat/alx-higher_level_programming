#!/usr/bin/python3
"""Deleting an element at an index"""


def delete_at(my_list=[], idx=0):
    length = len(my_list) - 1
    if (idx > length or idx < 0):
        return my_list
    else:
        del my_list[idx]
    return my_list
