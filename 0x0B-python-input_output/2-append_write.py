#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """append_write function
    this function appends the 'text' to file with 'filename'
    """
    with open(filename, mode='a', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)
