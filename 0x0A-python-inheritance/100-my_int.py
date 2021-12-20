#!/usr/bin/python3
"""Defines a class MyInt that inherit int"""


class MyInt(int):
    """Define class MyInt"""
    def __init__(self, value):
        """initialize the class
        Args:
            value (int): the value to be compare
        """
        self.value = value

    def __eq__(self, value):
        """Override == operator with !="""
        return self.real != self.value

    def __ne__(self, value):
        """Override != operator with ==="""
        return self.real == self.value
