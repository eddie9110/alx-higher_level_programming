#!/usr/bin/python3
"""
Class Square module
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square is a child class of Rectangle
    """

    def __init__(self, size):
        """
        Initialisation of Square class
        Args: size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
