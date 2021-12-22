#!/usr/bin/python3
import json
"""Defining function load_from_json_file"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read)
