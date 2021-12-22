#!/usr/bin/python3
"""Define a function read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): the file to be read.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
