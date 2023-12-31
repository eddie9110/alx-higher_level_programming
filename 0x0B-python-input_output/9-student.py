#!/usr/bin/python3
"""
A class Student Module
"""


class Student:
    """
    class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialising class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A Method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
