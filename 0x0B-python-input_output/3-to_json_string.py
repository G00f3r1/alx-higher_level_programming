import json
"""Define a function to_json_string"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)
    Args:
        my_obj (str): string object
    Return: JSON representation of an object (string)
    """
    return(json.dumps(my_obj))
