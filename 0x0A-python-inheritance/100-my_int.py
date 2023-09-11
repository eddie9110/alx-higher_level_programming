#!/usr/bin/python3
"""
Module of the class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __init__(self, value):
        """
        Initialising MyInt class
        """
        self.value = value

    def __eq__(self, other):
        """
        Method returns !=
        """
        return self.value != other

    def __ne__(self, other):
        """
        Method returns invert of ==
        """
        return self.value == other
