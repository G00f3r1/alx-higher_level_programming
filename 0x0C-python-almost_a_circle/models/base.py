#!/usr/bin/python3
"""Define Base Class """
import json
from os.path import exists


class Base:
    """Definition of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class
        Args:
            id (int): the id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes the JSON string representation
            of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open("Rectangle.json", "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string(None))
            lists = []
            for items in list_objs:
                lists.append(items.to_dictionary())
            file.write(cls.to_json_string(lists))

    def from_json_string(json_string):
        """function that returns the list of the JSON string representation
            json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 6)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """function that returns a list of instances"""
        file_name = cls.__name__ + ".json"

        if exists(file_name) is False:
            return []

        with open(file_name, mode="r", encoding="utf-8") as file:
            in_file = file.read()
            list_dictionary = cls.from_json_string(in_file)

            instances = []
            for items in list_dictionary:
                instances.append(cls.create(**items))
            return instances
