#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Definition of class Rectangle"""

    def __init__(self, width, height):
        """Initalize a new Rectangle
        Args:
            width (int): the widthe of the Rectangel.
            height (int): the height of the Rectangel.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the rectangle description"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
