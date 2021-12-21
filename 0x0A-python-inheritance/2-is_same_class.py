#!/usr/bin/python3
"""Defining function is_same_class"""


def is_same_class(obj, a_class):
    """This function cheks if an object is exactly an
        instance of the specified class
        Arg:
            obj(any): the object to be cheked
            a_class(type): the type to be cheked with
    """
    if type(obj) is a_class:
        return True
    else:
        False
