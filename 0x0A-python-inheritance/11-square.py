#!/usr/bin/python3
"""
class Square module
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square is a subclass of Rectangle
    """

    def __init__(self, size):
        """
        Initialisation of class Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
