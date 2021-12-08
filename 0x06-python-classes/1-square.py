#!/usr/bin/python3
"""Square Class

    A Square Class

"""


class Square:
    """Empty class with size private attribute
    """
    def __init__(self, size):
        """__init

        The __init__ method initalizes the size value of the square.

        Attributes:
            size (int): the size of the square.
        """
        self.__size = size
