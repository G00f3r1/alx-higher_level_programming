#!/usr/bin/python3
"""Defining a class called Rectangle"""


class Rectangle:
    """This Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Instantiation with width and height
        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the current width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value to width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the current height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value to height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Returns drawing representation of the Rectangle using #"""
        rect_str = ''

        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += str(self.print_symbol)
            if i != self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """Returns the representation of the Rectangle"""
        self.__width = str(eval('self.width'))
        self.__height = str(eval('self.height'))

        return 'Rectangle(' + self.__width + ', ' + self.__height + ')'

    def __del__(self):
        """Used to delete an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
