#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """write_file function
    this function writes the 'text' to file with 'filename'
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)
