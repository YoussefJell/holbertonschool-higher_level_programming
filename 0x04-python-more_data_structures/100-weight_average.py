#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    tuple_mult = 0
    if len(my_list) == 0:
        return 0
    for tuple in my_list:
        avg += tuple[1]
        tuple_mult += (tuple[0] * tuple[1])
    return tuple_mult / avg
