#!/usr/bin/python3
"""MyInt Module
this module swaps Eq and Ne, EVIL!"""


class MyInt(int):
    """MyInt
    this is myint class
    """

    def __eq__(self, other):
        """eq swap"""

        return super().__ne__(other)

    def __ne__(self, other):
        """ne swap"""
        return super().__eq__(other)
