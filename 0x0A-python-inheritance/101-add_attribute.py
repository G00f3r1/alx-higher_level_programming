#!/usr/bin/python3
"""Define funciton add_attribute"""


def add_attribute(obj, alttrb, value):
    """function that adds a new attribute to an object if it’s possible
    Args:
        obj (any): The object to add an attribute to
        alt (str): The name of the added attribute
        value (any): The value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, alttrb, value)
