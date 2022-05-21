#!/usr/bin/python3
"""5-text_indentation module
this module includes the function text_indentation
"""


def text_indentation(text):
    """text_indentation
    this function indents the text
    • text must be a string
    • There should be no space at the beginning or at the end of each printed line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_str = ""
    begin = 1
    i = 0

    while i < len(text):
        while text[i] == ' ' and begin == 1:
            i += 1
            continue

        begin = 0

        if text[i] in ['.', '?', ':']:
            new_str += text[i]
            new_str += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        if i < len(text):
            new_str += text[i]
            i += 1

    print(new_str, end='')
