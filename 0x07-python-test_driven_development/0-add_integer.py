#!/usr/bin/python3
"""This module Defines an integer additon function."""


def add_integer(a, b=98):
    """This function adds to integers and return a value
        Args:
            a (int, float): it have to be int or float
            b (int, float): it have to be int or float
        Returns:
            Returns the result of the addiion
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
