#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename, encoding='utf-8') as my_file:
        my_obj = json.loads(my_file.read())
    return my_obj
