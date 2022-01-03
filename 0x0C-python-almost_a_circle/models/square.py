#!/usr/bin/python3
"""Define the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class"""
        super().__init__(size, size, x, y)
        self.size = size

    def __str__(self):
        """Return the representation of Square"""
        return ("[Square] " + "(" + str(self.id) + ") " + str(self.x) +
                " / " + str(self.y) + " - " + str(self.width))

    @property
    def size(self):
        """Get the current size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """"Set the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the values of the Square using usint *args"""
        args_len = len(args)
        if args_len > 0:
            if args_len >= 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            if args_len == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            if args_len == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            if args_len == 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
