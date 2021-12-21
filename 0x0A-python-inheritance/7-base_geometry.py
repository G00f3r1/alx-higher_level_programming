#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Defining a class BaseGeometry"""
    def area(self):
        """This method is not implmented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validats value
        Args:
            name(str): the name of parameter
            value(int): the value that is validated
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
