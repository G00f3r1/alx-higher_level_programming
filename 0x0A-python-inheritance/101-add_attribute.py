#!/usr/bin/python3


def add_attribute(obj, alttrb, value):
    """Define a function add_attribute
    Args:
        obj (any): The object to add an attribute to
        alt (str): The name of the added attribute
        value (any): The value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, alttrb, value)
