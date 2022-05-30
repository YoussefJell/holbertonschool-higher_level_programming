#!/usr/bin/python3
"""Base Geometry
This includes BaseGeometry base class
and Rectangle which derives from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    this is the rectangle class
    """

    def __init__(self, width, height):
        """__init__
        this is the initialization of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
