#!/usr/bin/python3

import io
import sys
import unittest
from pathlib import Path

from models.base import Base
from models.square import Square


class TestRectInstantiation(unittest.TestCase):
    """Square class instantiation."""

    def test_no_argument_passed(self):
        """method test when 0 args are passed."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument_passed(self):
        """method tests if one argument is provided."""
        with self.assertRaises(TypeError):
            Square(5)

    def test_multi_args_passed(self):
        """
        method checks if TypeError is raised when over five arguments
        are passed
        """
        with self.assertRaises(TypeError):
            Square(5, 3, 2, 1, 4, 7)

    def test_inherits_base(self):
        """method to check if Square inherits from base class."""
        self.assertIsInstance(Square(2, 7), Base)

    def test_access_private_width(self):
        """
        method checks if AttributeError is raised when accessing private
        width attribute.
        """
        with self.assertRaises(AttributeError):
            print(Square(2, 1, 1, 3, 4).__width)

    def test_access_private_height(self):
        """
        method checks if AttributeError is raised when private height
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Square(2, 2, 0, 0, 3).__height)

    def test_access_private_x(self):
        """
        Method checks if AttributeError is raised when private x
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 0, 0, 1).__x)

    def test_access_private_y(self):
        """ method checks if AttributeError is raised when private y
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Square(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Method for testing Square width getter"""
        self.assertEqual(5, self.rect.width)

    def test_width_setter(self):
        """
        Method tests if the width setter updates the width attribute correctly.
        """
        self.rect.width = 6
        self.assertEqual(6, self.rect.width)

    def test_height_getter(self):
        """Test if the height getter returns the correct value."""
        self.assertEqual(7, self.rect.height)

    def test_height_setter(self):
        """Test if the height setter updates the height attribute correctly."""
        self.rect.height = 11
        self.assertEqual(11, self.rect.height)

    def test_getter_for_x(self):
        """Test if the x getter returns the correct value."""
        self.assertEqual(7, self.rect.x)

    def test_setter_for_x(self):
        """Test if the x setter updates the x attribute correctly."""
        self.rect.x = 12
        self.assertEqual(12, self.rect.x)

    def test_getter_for_y(self):
        """Test if the y getter returns the correct value."""
        self.assertEqual(5, self.rect.y)

    def test_setter_for_y(self):
        """Test if the y setter updates the y attribute correctly."""
        self.rect.y = 12
        self.assertEqual(12, self.rect.y)

    def test_area_single_arg(self):
        """Method tests for single arg passed """
        rect = Square(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(1)


class TestSquareWidth(unittest.TestCase):
    """Methods for testing Square width attribute."""

    def test_null_width(self):
        """Method tests if TypeError is raised
        when no argument is passed to the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)

    def test_neg_width_passed(self):
        """Method tests if TypeError is raised
        when negative no. is passed to the width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2, 4)

    def test_zero_width_passed(self):
        """Method checks if ValueError is raised when 0 is passed"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 3)

    def test_float_width_passed(self):
        """Method checks if TypeError is raised
        when a decimal number is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5, 1)

    def test_str_width_passed(self):
        """Method checks if TypeError
        is raised when a string is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("stng", 2)

    def test_width_complex_passed(self):
        """Method tests if TypeError is raised when a
        complex no. is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3), 2)

    def test_width_dict_passed(self):
        """method tests if TypeError is raised
        when a dictionary is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"key1": 4, "key2": 3}, 2)

    def test_list_width_passed(self):
        """method tests if TypeError is raised
        when a list is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([4, 1, 3], 2)

    def test_set_width_passed(self):
        """method tests if TypeError is raised
        when a set is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({4, 1, 3}, 2)

    def test_tuple_width_passed(self):
        """method tests if TypeError is raised
        when a tuple is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((4, 1, 3), 2)

    def test_inf_passed_width(self):
        """method tests if TypeError is raised
        when an infinite no is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("inf"), 2)

    def test_nan_passed_width(self):
        """method tests if TypeError is raised
        when nan is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("nan"), 2)


class TestSquareHeight(unittest.TestCase):
    """Methods for testing Square height attribute."""

    def test_negative_passed_height(self):
        """method tests if TypeError is raised
        when negative is passed as the height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Square(1, -1)

    def test_zero_passed_height(self):
        """method tests if TypeError is raised
        when zero is passed as the height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Square(1, 0)

    def test_none_passed_height(self):
        """method tests if TypeError is raised
        when none is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, None)

    def test_str_passed_height(self):
        """method tests if TypeError is raised
        when string is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, "stng")

    def test_float_passed_height(self):
        """method tests if TypeError is raised
        when a decimal no. is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(3, 5.4)

    def test_complex_passed_height(self):
        """method tests if TypeError is raised
        when a complex no. is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, complex(5))

    def test_dict_passed_height(self):
        """method tests if TypeError is raised
        when dict is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, {"key1": 1, "key2": 2})

    def test_list_passed_height(self):
        """method tests if TypeError is raised
        when a list is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_passed_height(self):
        """method tests if TypeError is raised
        when set is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_passed_height(self):
        """method tests if TypeError is raised
        when tuple is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, (1, 2, 3))

    def test_inf_passed_height(self):
        """method tests if TypeError is raised
        when inf is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, float("inf"))

    def test_nan_passed_height(self):
        """method tests if TypeError is raised
        when nan is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Square(1, float("nan"))


class TestSquareX(unittest.TestCase):
    """Methods for testing x attribute """

    def test_none_passed_x(self):
        """method tests if TypeError is raised
        when none is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, None)

    def test_str_passed_x(self):
        """method tests if TypeError is raised
        when a string is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, "stng", 2)

    def test_float_passed_x(self):
        """method tests if TypeError is raised
        when float is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, 5.5, 9)

    def test_complex_passed_x(self):
        """method tests if TypeError is raised
        when a complex no. is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, complex(5))

    def test_dict_passed_x(self):
        """method tests if TypeError is raised
        when a dictionary is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_passed_x(self):
        """method tests if TypeError is raised
        when a list is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, [1, 2, 3], 2)

    def test_set_passed_x(self):
        """method tests if TypeError is raised
        when a set is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, {1, 2, 3}, 2)

    def test_tuple_passed_x(self):
        """method tests if TypeError is raised
        when a tuple is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, (1, 2, 3), 2)

    def test_inf_passed_x(self):
        """method tests if TypeError is raised
        when an infinite float no is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, float("inf"), 2)

    def test_nan_passed_x(self):
        """method tests if TypeError is raised
        when nan is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 2, float("nan"), 2)

    def test_neg_passed_x(self):
        """method tests if TypeError is raised
        when a negative no. is passed as x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, 3, -1, 0)


class TestSquareY(unittest.TestCase):
    """Methods for testing initialization of y attribute."""

    def test_null_passed_y(self):
        """Method checks if typeError is raised when none is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 3, None)

    def test_negative_passed_y(self):
        """Method checks if typeError is raised when a negative is passed"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 3, 0, -9)

    def test_str_passed_y(self):
        """Method checks if typeError is raised when string is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, "stng")

    def test_float_passed_y(self):
        """Method checks if typeError is raised when a decimal no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 3, 5.5)

    def test_complex_passed_y(self):
        """Method checks if typeError is raised when a complex no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 3, complex(5))

    def test_dict_passed_y(self):
        """Method checks if typeError is raised when none is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, {"a": 1, "b": 2})

    def test_tuple_passed_y(self):
        """Method checks if typeError is raised when a tuple is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, (1, 2, 3))

    def test_list_passed_y(self):
        """Method checks if typeError is raised when list is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, [1, 2, 3])

    def test_set_passed_y(self):
        """Method checks if typeError is raised when a set is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, {1, 2, 3})

    def test_nan_passed_y(self):
        """Method checks if typeError is raised when nan is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, float("nan"))

    def test_infinte_y(self):
        """Method checks if typeError is
        raised when an infinite no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 1, float("inf"))


class TestSquareDisplay(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def rdout(sq, metd):
        """aquires and returns text printed to stdout.
        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout
        """
        otpt = io.StringIO()
        sys.stdout = otpt
        if metd == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return otpt

    def test_str_mtd_print_size(self):
        sqr = Square(4)
        otpt = TestSquareDisplay.rdout(sqr, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sqr.id)
        self.assertEqual(correct, otpt.getvalue())

    def test_str_mtd_size_x(self):
        sqr = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(sqr.id)
        self.assertEqual(correct, sqr.__str__())

    def test_str_mtd_size_x_y(self):
        sqr = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(sqr.id)
        self.assertEqual(correct, str(s))

    def test_str_mtd_size_x_y_id(self):
        sqr = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sqr))

    def test_str_mtd_changed_attributes(self):
        sqr = Square(7, 0, 0, [4])
        sqr.size = 15
        sqr.x = 8
        sqr.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sqr))

    def test_str_mtd_one_arg(self):
        sqr = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sqr.__str__(1)

    def test_size_display(self):
        sqr = Square(2, 0, 0, 9)
        otpt = TestSquareDisplay.rdout(sqr, "display")
        self.assertEqual("##\n##\n", otpt.getvalue())

    def test_size_x_display(self):
        sqr = Square(3, 1, 0, 18)
        otpt = TestSquareDisplay.rdout(sqr, "display")
        self.assertEqual(" ###\n ###\n ###\n", otpt.getvalue())

    def test_size_y_display(self):
        sqr = Square(4, 0, 1, 9)
        otpt = TestSquareDisplay.rdout(sqr, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, otpt.getvalue())

    def test_size_x_y_display(self):
        sqr = Square(2, 3, 2, 1)
        otpt = TestSquareDisplay.rdout(sqr, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, otpt.getvalue())

    def test_one_arg_display(self):
        sqr = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sqr.display(1)


if __name__ == "__main__":
    unittest.main()
