#!/usr/bin/python3
"""Square class

Defines a square class
and has private instance size

"""


class Square:
    """Square Class
    This square has a size
    """

    def __init__(self, size=0):
        """__init__
        initializing square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
