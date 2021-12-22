#!/usr/bin/python3
"""Define function write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
        and returns the number of characters written
    Args:
        filename (str): the file name to be written in to.
        text (str): the text to be written.
    Return:
        Number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
