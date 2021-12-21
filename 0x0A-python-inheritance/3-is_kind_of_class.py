#!/usr/bin/python3
"""Define a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """This function cheks  if the object is an instance
        of object or inherited instance of a class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
