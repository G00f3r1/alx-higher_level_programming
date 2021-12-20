#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a class Square that inherit Rectangle"""


class Square(Rectangle):
    """Defines a class Square"""
    def __init__(self, size):
        """Initalize a square
        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
