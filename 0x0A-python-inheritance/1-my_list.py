#!/usr/bin/python3
"""
A module of MyList class
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        A function that prints the list, but sorted (ascending sort)
        Args:
            self
        """
        print(sorted(self))
