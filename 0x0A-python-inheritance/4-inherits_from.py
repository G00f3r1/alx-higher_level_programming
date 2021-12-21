#!/usr/bin/python3
"""Define function inherits_from"""


def inherits_from(obj, a_class):
    """This function cheks if an object is an inherited instance of a class"""
    if (isinstance(type(obj), a_class) and
            type(obj) != a_class):
        return True
    else:
        return False
