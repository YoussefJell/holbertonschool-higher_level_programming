#!/usr/bin/python3
import json
"""from_json_string module"""


def from_json_string(my_str):
    """from_json_string function
    returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
