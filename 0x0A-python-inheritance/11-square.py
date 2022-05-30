#!/usr/bin/python3
"""Base Geometry
This includes BaseGeometry base class
and Rectangle which derives from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    this class inherits from Rectangle
    """

    def __init__(self, size):
        """__init__ method
        this method initializes the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """__str__ method
        this method executes upon printing the instance
        """
        return f"[Square] {self.__size}/{self.__size}"
