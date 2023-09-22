#!/usr/bin/python3
"""
Module for the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialising a Rectangle object

        Args:
            width: width of a rectangle
            height: height of a rectangle
            x: The x-coordinate of the rectangle's position
            y: The y-coordinate of the rectangle's position
            id: The ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        A getter for the private attribute __width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method and validation
        for the private attribute __width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        A getter mtd for the private attribute __height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        A setter method plus validation
        for the private atttribute __height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        A getter method for the private attribute __x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        a setter method plus validation
          for private attribute __x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        A getter method for the private attribute __y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        a setter method plus validation
          for the private attribute __y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """This method prints the Rectangle using the # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
    [print("") for y in range(self.y)]
    for ht in range(self.height):
        for x in range(self.x):
            print(" ", end="")
        for wd in range(self.width):
            print("#", end="")
        print("")

    def __str__(self):
        """
        Method will return a string representation of the square object.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        this method updates the attributes of rectangle object.

        Args:
            *args: arguments represent attribute values.
            **kwargs: KW arguments represent attribute-value pairs.
        """
        if len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            d = 0
            for arg in args:
                setattr(self, attrs[d], arg)
                d += 1
        elif len(kwargs) > 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        This method returns a dictionary
        representation of the rectangle object.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
