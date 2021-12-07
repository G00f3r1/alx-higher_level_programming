#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._size = size
        self._position = position

    def area(self):
        return self._size ** 2

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                for p in range(self._position[0]):
                    print(" ", end='')
                for j in range(self._size):
                    print("#", end='')
                print()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
