#!/usr/bin/python3
import json
"""load_from_json_file module"""


def load_from_json_file(filename):
    """load_from_json_file function
    creates an Object from a “JSON file”
    """
    with open(filename, encoding='utf-8') as my_file:
        my_obj = json.loads(my_file.read())
    return my_obj
