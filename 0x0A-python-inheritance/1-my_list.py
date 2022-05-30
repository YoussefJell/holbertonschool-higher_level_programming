#!/usr/bin/python3
"""MyList Class
class for my list
"""


class MyList(list):
    """MyList class
    this class inherits from the list class
    """

    def print_sorted(self):
        print(sorted(self))
