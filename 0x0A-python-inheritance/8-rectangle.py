#!/usr/bin/python3
"""Define a class Rectangle that inherit BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of a class Rectangle"""

    def __init__(self, width, height):
        """Initalize the class Rectangle
        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
