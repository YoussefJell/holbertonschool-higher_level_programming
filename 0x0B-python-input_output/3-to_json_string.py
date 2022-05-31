#!/usr/bin/python3
import json
"""to_json_string module"""


def to_json_string(my_obj):
    """to_json_string function
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
