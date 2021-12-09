#!/usr/bin/python3
"""Definine Square Class"""


class Square:
    """Square Class
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initializes the size value of the square.

        Attributes:
            size (int): The size of the square.
            position (int): tuple of 2 positive integers

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.position = position

    def area(self):
        """area

        Returns the current square area

        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size

        The size setter method update the size value of the square.

        Attributes:
            value (int): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) or type(value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for p in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
