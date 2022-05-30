#!/usr/bin/python3
"""BaseGeometry class
Has method that is not yet implemented
"""


class BaseGeometry:
    """BaseGeometry class
    Methods:
        area: Measures area (not yet implemented)
    """

    def area(self):
        """area method
        this method is not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator
        this validates an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
