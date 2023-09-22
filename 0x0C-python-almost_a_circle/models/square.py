#!/usr/bin/python3

"""
class Square that inherits from Rectangle:

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inherits from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Copying the attributes form class rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method to add size attribute
        aka size of the square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        setter for new attribute size
        for the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            this method updates the attributes of square object.

            Args:
            *args: arguments represent attribute values.
            **kwargs: KW arguments represent attribute-value pairs.
        """

    if len(args) > 0:
        attrs = ["id", "size", "x", "y"]
        u = 0
        for arg in args:
            setattr(self, attrs[u], arg)
            u += 1
        return
    for key in kwargs:
        setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Method will return a dictionary representation of the square object.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Method will return a string representation of the square object.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
