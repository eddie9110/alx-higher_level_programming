#!/usr/bin/python3
"""
Rectangle class Module
"""


class Rectangle:
    """
    Class named Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle Class initialiser

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Height getter

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle

        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
