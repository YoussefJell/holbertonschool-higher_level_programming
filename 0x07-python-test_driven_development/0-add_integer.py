#!/usr/bin/python3
"""0-add_integer Module
This module is for adding the variable 'a' and 'b' together\
"""


def add_integer(a, b=98):
    """add_integer function

    this function adds var 'a' to var 'b'
    the variables 'a' and 'b' have to be of type int or float
    incase 'a' or 'b' is a float it will be converted to an integer
    the return value is the a + b and is an integer

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
