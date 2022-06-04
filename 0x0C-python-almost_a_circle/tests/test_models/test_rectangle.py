#!/usr/bin/python3
"""Unittest for rectangle.py
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class
    this class is to test the Rectangle class from models/rectangle.py
    """

    def test_pep8(self):
        """test_pep8 method
        this method tests if the function is properly
        styled
        """
        style = pep8.StyleGuide()
        check = style.check_files(["models/rectangle.py"])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 STYLE ERROR IN RECTANGLE")

    def test_wrong_params_rectangle(self):
        """test_empty_rectangle method
        this method tests the rectangle class
        """
        self.assertRaises(TypeError, Rectangle, 'string', 'string2')

    def test_correct_params(self):
        """test_correct_params method
        this method tests if the getters and setters work
        """
        rect1 = Rectangle(3, 5)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 5)

        rect2 = Rectangle(4, 2, 3, 3)
        self.assertEqual(rect2.width, 4)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 3)

        rect3 = Rectangle(10, 8, 1, 1, 47)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.height, 8)
        self.assertEqual(rect3.x, 1)
        self.assertEqual(rect3.y, 1)
        self.assertEqual(rect3.id, 47)

    def test_param_negative(self):
        """test_param_negative method
        this method tests if the class properly raises an error
        with negative numbers
        """
        self.assertRaises(ValueError, Rectangle, 4, -2)
        self.assertRaises(ValueError, Rectangle, 4, 3, 0, -1)

    def test_param_float(self):
        """test_param_float method
        this method tests if the class properly raises an error
        with floating points
        """
        self.assertRaises(TypeError, Rectangle, 4, 1.5)
        self.assertRaises(TypeError, Rectangle, 4, 3, 2.5, 1)
        self.assertRaises(TypeError, Rectangle, 4, 3, 2, 1.01)
        self.assertRaises(TypeError, Rectangle, 4.4, 3, 2, 1)

    def test_param_bool(self):
        """test_param_bool method
        this method tests if the class properly raises an error
        with boolean ops
        """
        self.assertRaises(TypeError, Rectangle, 4, True)
        self.assertRaises(TypeError, Rectangle, 4, 3, False)

    def test_area(self):
        """test_area method
        this method tests if the class properly calculates
        the area
        """
        my_rect = Rectangle(5, 4)
        self.assertEqual(my_rect.area(), 20)
        my_rect2 = Rectangle(3, 9)
        self.assertEqual(my_rect2.area(), 27)
