#!/usr/bin/python3
"""
Module to create a class Rectangle
"""


class Rectangle:
    """
    Class named Rectangle
    """

    no_instances = 0

    def __init__(self, width=0, height=0):
        """
        Class initializer

        Args:
            self : Arg
            width : Arg
                (default 0)
            height : Argument
                (default 0)

        """
        self.height = height
        self.width = width
        Rectangle.no_instances += 1

    @property
    def width(self):
        """
        Width getter ftn

        Args:
            self : Argument

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter ftn

        Args:
            self : Arg
            value : Arg

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter ftn

        Args:
            self : Arg

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter ftn

        Args:
            self : Arg
            value : Arg

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of rectangle

        Args:
            self : Arg

        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns perimeter of rectangle

        Args:
            self : Argument

        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        Returns rectangle with the character # as string

        Args:
            self : Argument

        """
        if self.height == 0 or self.width == 0:
            return ""
        rec = ""
        for ok in range(self.height):
            for mo in range(self.width):
                rec += "#"
            if ok != self.height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """
        Returns a string representation of the rectangle

        Args:
            self : Arg
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of class rectangle is deleted

        Args:
            self : Arg

        """
        Rectangle.no_instances -= 1
        print("Bye rectangle...")
