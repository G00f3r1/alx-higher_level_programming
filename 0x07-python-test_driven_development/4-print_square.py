#!/usr/bin/python3
"""This module say_my_name function"""


def print_square(size):
    """This is function that prints a square with the character #
        Args:
            size (int): the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
