#!/usr/bin/python3
"""
    module defines Square class with a private instance
    attribute
"""


class Square:
    """ class definition for square. """
    def __init__(self, size=0):
        """
        Args:
            size (int): length of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Returns the square area. """
        return self.__size**2
