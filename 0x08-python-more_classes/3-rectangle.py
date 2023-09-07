#!/usr/bin/python3
"""
    Rectangle class module
"""


class Rectangle:
    """
    Rectangle class

    """

    def __init__(self, width=0, height=0):
        """
        Initialising a rectangle class.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter function for private variable, width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter function for height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private variable, height.

        Args:
            self: arg
            value: height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
