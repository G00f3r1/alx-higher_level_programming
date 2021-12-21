#!/usr/bin/python3
"""Define class Square that inherit Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class Square"""
    def __init__(self, size):
        """Initialize the Square
        Args:
            size (int): the size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return the square description"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
