#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for a_key, a_value in a_dictionary.items():
        if a_value == value:
            new_list.append(a_key)
    for elem in new_list:
        del a_dictionary[elem]
    return a_dictionary
