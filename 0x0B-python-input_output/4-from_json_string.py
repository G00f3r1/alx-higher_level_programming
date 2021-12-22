#!/usr/bin/python3
import json
"""Define a function to_json_string"""


def from_json_string(my_obj):
    """function that returns an object (Python data structure)
        represented by a JSON string
    Args:
        my_obj (str): string object
    Return: returns an object represented by a JSON string
    """
    return json.loads(my_obj)
