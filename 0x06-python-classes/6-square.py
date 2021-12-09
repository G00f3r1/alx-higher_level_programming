#!/usr/bin/python3
"""Definine Square Class"""


class Square:
    """ Square Class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
                Instantiation with size
        Args:
            size: size of the square
            position: postion of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print a square with the # character"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position to value."""
        if (type(value) != tuple or len(value) != 2 or
                isinstance(value[0], int) is False or
                isinstance(value[1], int) is False or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
