#!/usr/bin/python3
"""define a funcction find_peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if type(list_of_integers) != list:
        return
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
