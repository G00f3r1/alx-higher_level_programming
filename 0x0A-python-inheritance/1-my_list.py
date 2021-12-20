#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """definition of class MyList"""
    def print_sorted(self):
        print(sorted(self))
