#!/usr/bin/python3
import json
"""Define a function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
        using a JSON representation
    Args:
        my_obj (obj): the object to be written to the file
        filename (str): text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
