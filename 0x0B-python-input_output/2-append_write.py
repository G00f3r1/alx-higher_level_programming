#!/usr/bin/python3
"""Define function append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
        (UTF8) and returns the number of characters added.
    Args:
        filename (str): the file the string is to be added on.
        text (str): the string to be add.
    Return: returns the number of characters added
    """
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
