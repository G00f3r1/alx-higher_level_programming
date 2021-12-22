#!/usr/bin/python3
"""Define function class_to_json"""


def class_to_json(obj):
    """ function that returns the dictionary description
        with simple data structure for JSON serialization of an object
    Args:
        obj (obj):  instance of a Class
    """
    return obj.__dict__
