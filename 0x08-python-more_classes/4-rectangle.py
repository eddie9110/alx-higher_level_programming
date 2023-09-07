#!/usr/bin/python3
"""
    Define a Rectangle class with width and height.
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Class initialiser

        Args:
            width :  Defaults 0.
            height : Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter function for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for width.

        Args:
            value : arg
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter function height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value : arg.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """calculate the perimeter of the rectangle."""
        if any((self.height == 0, self.width == 0)):
            return 0
        return 2*(self.height + self.width)

    def __str__(self):
        """
        draws a rectangle with the character #

        """
        if self.height == 0 or self.width == 0:
            return ""
        square = ""
        for fg in range(self.height):
            for gh in range(self.width):
                square += "#"
            if fg != self.height - 1:
                square += "\n"
        return square

    def __repr__(self):
        """
        Returns a string representation of rectangle
        Args:
            self : arg

        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
