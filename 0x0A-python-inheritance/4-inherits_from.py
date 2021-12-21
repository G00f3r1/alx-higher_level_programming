#!/usr/bin/python3


def inherits_from(obj, a_class):
    """This function cheks if an object is an inherited instance of a class"""
    if (isinstance(obj, a_class) and
            isinstance(a_class, obj.__class__) is False):
        return True
    else:
        False
