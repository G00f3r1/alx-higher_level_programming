#!/usr/bin/python3
import dis
import math
"""MagicClass
"""

class MagicClass:
    """MagicClass
    """
    def __init__(self, radius=0):
        """__init__
        The __init__ method initializes the size value of the square.

        Attributes:
            radius (int): The size of the square.

        Raises:
            TypeError: If `radius` type is not `number`.

        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
