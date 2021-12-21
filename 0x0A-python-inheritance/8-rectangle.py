#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a class Rectangle that inherit BaseGeometry"""


class Rectangle(BaseGeometry):
    """Definition of a class Rectangle"""
    def __init__(self, width, height):
        """this instantiate the class with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
