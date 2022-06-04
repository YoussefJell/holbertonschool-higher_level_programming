#!/usr/bin/python3
"""Unittest for Square.py
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare class
    this class is to test the Square class from models/Square.py
    """

    def test_pep8(self):
        """test_pep8 method
        this method tests if the function is properly
        styled
        """
        style = pep8.StyleGuide()
        check = style.check_files(["models/square.py"])
        self.assertEqual(check.total_errors, 0, "PEP8 STYLE ERROR IN BASE")

    def test_wrong_params_Square(self):
        """test_empty_Square method
        this method tests the Square class
        """
        self.assertRaises(TypeError, Square, 'string', 'string2')

    def test_square_w_h(self):
        """test_square_w_h method
        this method tests if the width and height are correctly set
        """
        sqr1 = Square(3)
        sqr1.size = 4
        self.assertEqual(sqr1.width, 4)
        self.assertEqual(sqr1.height, 4)

    def test_correct_params(self):
        """test_correct_params method
        this method tests if the getters and setters work
        """
        sqr1 = Square(1)
        sqr1.size = 3
        self.assertEqual(sqr1.size, 3)

        sqr2 = Square(4, 3, 3)
        sqr2.size = 4
        self.assertEqual(sqr2.size, 4)
        self.assertEqual(sqr2.x, 3)
        self.assertEqual(sqr2.y, 3)

        sqr3 = Square(10, 1, 1, 47)
        sqr2.size = 10
        self.assertEqual(sqr3.size, 10)
        self.assertEqual(sqr3.x, 1)
        self.assertEqual(sqr3.y, 1)
        self.assertEqual(sqr3.id, 47)

    def test_param_negative(self):
        """test_param_negative method
        this method tests if the class properly raises an error
        with negative numbers
        """
        self.assertRaises(ValueError, Square, 4, -2)
        self.assertRaises(ValueError, Square, 4, 3, -1)

    def test_param_float(self):
        """test_param_float method
        this method tests if the class properly raises an error
        with floating points
        """
        self.assertRaises(TypeError, Square, 4, 1.5)
        self.assertRaises(TypeError, Square, 4, 2.5, 1)
        self.assertRaises(TypeError, Square, 4, 2, 1.01)
        self.assertRaises(TypeError, Square, 4.3, 2, 1)

    def test_param_bool(self):
        """test_param_bool method
        this method tests if the class properly raises an error
        with boolean ops
        """
        self.assertRaises(TypeError, Square, 4, True)
        self.assertRaises(TypeError, Square, 4, 3, False)

    def test_todict(self):
        sqr1 = Square(4, 1, 1, 50)
        my_dict = {"id": 50, "size": 4, "x": 1, "y": 1}
        self.assertEqual(sqr1.to_dictionary(), my_dict)
