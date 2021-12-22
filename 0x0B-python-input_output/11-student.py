#!/usr/bin/python3
"""Defin class Student"""


class Student:
    """class definition named Student"""
    def __init__(self, first_name, last_name, age):
        """initializ the class
        Args:
            first_name (str): First name of the student
            last_name (str: Second for student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) != str:
                    return class_b
                if attr in class_d:
                    sel_d[attr] = class_d[attr]
            return sel_d
        return class_d

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
