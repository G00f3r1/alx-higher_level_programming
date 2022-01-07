#!/usr/bin/python3
"""Define Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Definition of the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class Rectangle
        Args:
            width (int): the width of Rectangle
            height (int): the height of Rectangle
            x (int): the x (position from the side) of Rectangle
            y (int): the y (position from the top) of Rectangle
            id (int): the id of Rectangle
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the current width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the current x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the current y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y of the Rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the Rectangle with the character #"""
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return the representation of the Rectangle"""
        return ("[Rectangle] " + "(" + str(self.id) + ") " +
                str(self.__x) + "/" + str(self.__y) + " - " +
                str(self.__width) + "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """Update the values of the Rectangle using usint *args"""
        args_len = len(args)
        if args_len > 0:
            if args_len >= 5:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                if type(args[2]) is not int:
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                if type(args[3]) is not int:
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                if type(args[4]) is not int:
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                super().__init__(args[0])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            if args_len == 4:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                if type(args[2]) is not int:
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                if type(args[3]) is not int:
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                super().__init__(args[0])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if args_len == 3:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                if type(args[2]) is not int:
                    raise TypeError("height must be an integer")
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                super().__init__(args[0])
                self.__width = args[1]
                self.__height = args[2]
            if args_len == 2:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                super().__init__(args[0])
                self.__width = args[1]
            if args_len == 1:
                super().__init__(args[0])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    if type(value) is not int:
                        raise TypeError(key + " must be an integer")
                    if value <= 0:
                        raise ValueError(key + " must be > 0")
                    self.__width = value
                if key == "height":
                    if type(value) is not int:
                        raise TypeError(key + " must be an integer")
                    if value <= 0:
                        raise ValueError(key + " must be > 0")
                    self.__height = value
                if key == "x":
                    if type(value) is not int:
                        raise TypeError(key + " must be an integer")
                    if value <= 0:
                        raise ValueError(key + " must be >= 0")
                    self.__x = value
                if key == "y":
                    if type(value) is not int:
                        raise TypeError(key + " must be an integer")
                    if value <= 0:
                        raise ValueError(key + " must be >= 0")
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return ({"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width})
