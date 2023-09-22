#!/usr/bin/python3

import io
import sys
import unittest
from pathlib import Path

from models.base import Base
from models.rectangle import Rectangle


class TestRectInstantiation(unittest.TestCase):
    """Rectangle class instantiation."""

    def test_no_argument_passed(self):
        """method test when 0 args are passed."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument_passed(self):
        """method tests if one argument is provided."""
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_multi_args_passed(self):
        """
        method checks if TypeError is raised when over five arguments
        are passed
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 2, 1, 4, 7)

    def test_inherits_base(self):
        """method to check if rectangle inherits from base class."""
        self.assertIsInstance(Rectangle(2, 7), Base)

    def test_access_private_width(self):
        """
        method checks if AttributeError is raised when accessing private
        width attribute.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 1, 1, 3, 4).__width)

    def test_access_private_height(self):
        """
        method checks if AttributeError is raised when private height
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 3).__height)

    def test_access_private_x(self):
        """
        Method checks if AttributeError is raised when private x
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_access_private_y(self):
        """ method checks if AttributeError is raised when private y
        attribute is accessed.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Method for testing Rectangle width getter"""
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
        rect = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(1)


class TestRectangleWidth(unittest.TestCase):
    """Methods for testing Rectangle width attribute."""

    def test_null_width(self):
        """Method tests if TypeError is raised
        when no argument is passed to the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_neg_width_passed(self):
        """Method tests if TypeError is raised
        when negative no. is passed to the width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_zero_width_passed(self):
        """Method checks if ValueError is raised when 0 is passed"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def test_float_width_passed(self):
        """Method checks if TypeError is raised
        when a decimal number is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 1)

    def test_str_width_passed(self):
        """Method checks if TypeError
        is raised when a string is passed"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("stng", 2)

    def test_width_complex_passed(self):
        """Method tests if TypeError is raised when a
        complex no. is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 2)

    def test_width_dict_passed(self):
        """method tests if TypeError is raised
        when a dictionary is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key1": 4, "key2": 3}, 2)

    def test_list_width_passed(self):
        """method tests if TypeError is raised
        when a list is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 1, 3], 2)

    def test_set_width_passed(self):
        """method tests if TypeError is raised
        when a set is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 1, 3}, 2)

    def test_tuple_width_passed(self):
        """method tests if TypeError is raised
        when a tuple is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 1, 3), 2)

    def test_inf_passed_width(self):
        """method tests if TypeError is raised
        when an infinite no is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 2)

    def test_nan_passed_width(self):
        """method tests if TypeError is raised
        when nan is passed as the width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 2)


class TestRectangleHeight(unittest.TestCase):
    """Methods for testing Rectangle height attribute."""

    def test_negative_passed_height(self):
        """method tests if TypeError is raised
        when negative is passed as the height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_passed_height(self):
        """method tests if TypeError is raised
        when zero is passed as the height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_none_passed_height(self):
        """method tests if TypeError is raised
        when none is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_passed_height(self):
        """method tests if TypeError is raised
        when string is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "stng")

    def test_float_passed_height(self):
        """method tests if TypeError is raised
        when a decimal no. is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 5.4)

    def test_complex_passed_height(self):
        """method tests if TypeError is raised
        when a complex no. is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_passed_height(self):
        """method tests if TypeError is raised
        when dict is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"key1": 1, "key2": 2})

    def test_list_passed_height(self):
        """method tests if TypeError is raised
        when a list is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_passed_height(self):
        """method tests if TypeError is raised
        when set is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_passed_height(self):
        """method tests if TypeError is raised
        when tuple is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_inf_passed_height(self):
        """method tests if TypeError is raised
        when inf is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

    def test_nan_passed_height(self):
        """method tests if TypeError is raised
        when nan is passed as the height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("nan"))


class TestRectangleX(unittest.TestCase):
    """Methods for testing x attribute """

    def test_none_passed_x(self):
        """method tests if TypeError is raised
        when none is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an inegert"):
            Rectangle(1, 2, None)

    def test_str_passed_x(self):
        """method tests if TypeError is raised
        when a string is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "stng", 2)

    def test_float_passed_x(self):
        """method tests if TypeError is raised
        when float is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_passed_x(self):
        """method tests if TypeError is raised
        when a complex no. is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_passed_x(self):
        """method tests if TypeError is raised
        when a dictionary is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_passed_x(self):
        """method tests if TypeError is raised
        when a list is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_passed_x(self):
        """method tests if TypeError is raised
        when a set is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_passed_x(self):
        """method tests if TypeError is raised
        when a tuple is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_inf_passed_x(self):
        """method tests if TypeError is raised
        when an infinite float no is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("inf"), 2)

    def test_nan_passed_x(self):
        """method tests if TypeError is raised
        when nan is passed as x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("nan"), 2)

    def test_neg_passed_x(self):
        """method tests if TypeError is raised
        when a negative no. is passed as x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangleY(unittest.TestCase):
    """Methods for testing initialization of y attribute."""

    def test_null_passed_y(self):
        """Method checks if typeError is raised when none is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_negative_passed_y(self):
        """Method checks if typeError is raised when a negative is passed"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 0, -9)

    def test_str_passed_y(self):
        """Method checks if typeError is raised when string is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "stng")

    def test_float_passed_y(self):
        """Method checks if typeError is raised when a decimal no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_passed_y(self):
        """Method checks if typeError is raised when a complex no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_passed_y(self):
        """Method checks if typeError is raised when none is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_tuple_passed_y(self):
        """Method checks if typeError is raised when a tuple is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_list_passed_y(self):
        """Method checks if typeError is raised when list is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_passed_y(self):
        """Method checks if typeError is raised when a set is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_nan_passed_y(self):
        """Method checks if typeError is raised when nan is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("nan"))

    def test_infinte_y(self):
        """Method checks if typeError is
        raised when an infinite no. is passed"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("inf"))


class TestRectangleDisplay(unittest.TestCase):
    """Methods for testing str() and display methods of Rectangle class."""

    @staticmethod
    def rdout(rect, metd):
        """Gets and returns text to print to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            metd (str): The method to run on rect.
        Return:
            The text printed to stdout.
        """
        otpt = io.StringIO()
        sys.stdout = otpt

        if metd == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return otpt

    def test_display_w_h(self):
        """..."""
        rec = Rectangle(2, 3, 0, 0, 0)
        otpt = TestRectangleDisplay.rdout(rec, "display")
        self.assertEqual("##\n##\n##\n", otpt.getvalue())

    def test_display_w_h_x(self):
        """..."""
        rec = Rectangle(4, 2, 1, 0, 1)
        otpt = TestRectangleDisplay.rdout(rec, "display")
        self.assertEqual(" ####\n ####\n", otpt.getvalue())

    def test_display_w_h_y(self):
        """..."""
        rec = Rectangle(4, 5, 0, 1, 0)
        otpt = TestRectangleDisplay.rdout(rec, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, otpt.getvalue())

    def test_display_w_h_x_y(self):
        """..."""
        rec = Rectangle(3, 4, 3, 2, 0)
        otpt = TestRectangleDisplay.rdout(rec, "display")
        display = "\n\n   ###\n   ###\n   ###\n   ###\n"
        self.assertEqual(display, otpt.getvalue())

    def test_display_one_arg(self):
        """..."""
        rec = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rec.display(1)

    def test_str_mtd_print_wdh_ht(self):
        """..."""
        rec = Rectangle(4, 6)
        otpt = TestRectangleDisplay.rdout(r, "print")
        p_out = "[Rectangle] ({}) 0/0 - 4/6\n".format(rec.id)
        self.assertEqual(p_out otpt.getvalue())

    def test_str_mtd_wdh_ht_x(self):
        """..."""
        rec = Rectangle(5, 5, 1)
        p_out = "[Rectangle] ({}) 1/0 - 5/5".format(rec.id)
        self.assertEqual(p_out, rec.__str__())

    def test_str_mtd_wdh_ht_x_y(self):
        """..."""
        rec = Rectangle(1, 8, 2, 4)
        p_out = "[Rectangle] ({}) 2/4 - 1/8".format(rec.id)
        self.assertEqual(p_out, str(rec))

    def test_str_mtd_wdh_ht_x_y_id(self):
        """..."""
        rec = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rec))

    def test_str_mtd_changed_atts(self):
        """..."""
        rec = Rectangle(7, 7, 0, 0, [4])
        rec.width = 15
        rec.height = 1
        rec.x = 8
        rec.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rec))

    def test_str_mtd_one_arg(self):
        """..."""
        rec = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rec.__str__(1)


if __name__ == "__main__":
    unittest.main()
