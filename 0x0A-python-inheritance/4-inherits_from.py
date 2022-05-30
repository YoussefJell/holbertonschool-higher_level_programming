#!/usr/bin/python3
"""
Checks if object's class inherits from another class
"""


def inherits_from(obj, a_class):
    """inherits_from function
    this function checks for inheritance
    """
    return issubclass(obj.__class__, a_class) and type(obj) != a_class
