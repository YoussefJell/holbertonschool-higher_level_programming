#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = list(a_dictionary.values())
    max_key = list(a_dictionary.keys())
    return max_key[max_val.index(max(max_val))]
