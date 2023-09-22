#!/usr/bin/python3
"""Module for Unit Tests for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class represents tests for the Base class"""

    def test_doc(self):
        """
        Method tests for the presence of module documentation
        """
        self.assertIsNotNone(Base.__doc__)

    def test_class_doc_presence(self):
        """
        Method tests for the Base class documentation
        """
        self.assertIsNotNone(Base.__doc__)

    def test_init_doc_presence(self):
        """
        Method tests for documentation in __init__
        """
        self.assertIsNotNone(Base.__init__.__doc__)

    def test_to_json_string_doc(self):
        """
        Method tests for documentation in the to json string method
        """
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_init_with_id(self):
        """This method initialises Base instance with an ID"""
        bs = Base(114)
        self.assertEqual(bs.id, 114)

    def test_init_minus_id(self):
        """Method initialises Base instances without ID"""
        bs_1 = Base()
        bs_2 = Base()
        self.assertEqual(bs_1.id, 1)
        self.assertEqual(bs_2.id, 2)

    def test_multiple_instances(self):
        """This method tests multiple instances of Base with and without ID."""
        bs_1 = Base()
        bs_2 = Base()
        bs_3 = Base(136)
        self.assertEqual(bs_1.id, 3)
        self.assertEqual(bs_2.id, 4)
        self.assertEqual(bs_3.id, 136)

    def test_to_json_string(self):
        """This method tests the to_json_string method of Base."""
        self.assertEqual(Base.to_json_string([]), "[]")
        ld1 = Base.to_json_string([{'id': 13, 'name': 'json'}])
        self.assertEqual(ld1, '[{"id": 13, "name": "json"}]')
        ld2 = Base.to_json_string([{'id': 13, 'name': 'json'},
                                   {'age': 12, 'class': 4}])
        self.assertEqual(ld2, '[{"id": 13, "name": "json"}, '
                         '{"age": 12, "class": 4}]')
        self.assertIsInstance(ld2, str)

    def test_from_json_string(self):
        """Test the from_json_string method of Base."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        dc1 = Base.from_json_string('[{"id": 13, "name": "json"}]')
        self.assertEqual(dc1, [{'id': 13, 'name': 'json'}])
        dc2 = Base.from_json_string('[{"id": 18, "name": "json"}, '
                                    '{"age": 19, "class": 4}]')
        self.assertEqual(dc2, [{'id': 18, 'name': 'json'},
                               {'age': 19, 'class': 4}])
        self.assertIsInstance(dc2, list)


if __name__ == '__main__':
    unittest.main()
