#!/usr/bin/python3
"""
no imported module
"""
def find_peak(list_of_integers):
    """
    function to find the peak value from a
    given list
    """
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 0:
        return None
    elif size == 1:
        return (list_of_integers)
    elif size == 2:
        return max(list_of_integers)
    mid = int(size/2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1 :])
