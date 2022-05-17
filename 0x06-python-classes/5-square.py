#!/usr/bin/python3
"""Square class

Defines a square class
and has private instance size

"""


class Square:
    """Square Class
    This square has a size an area a setter and a getter and a printer
    """

    def __init__(self, size=0):
        """__init__
        initializing square
        """
        self.__size = size

    def area(self):
        """area
        returns area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print
        prints the square
        """
        if self.__size == 0:
            print()
            return None

        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
