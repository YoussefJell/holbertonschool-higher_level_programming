#!/usr/bin/python3
"""4-print_square module
this module includes a function that prints a square
"""


def print_square(size):
    """print_square function
    this function will print a square according to the argument size

    • size must be a positive integer bigger than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
