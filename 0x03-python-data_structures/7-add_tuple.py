#!/usr/bin/python3
def tuple_func(my_Tuple=()):
    if len(my_Tuple) < 2:
        if len(my_Tuple) == 1:
            my_Tuple = (my_Tuple[0], 0)
        elif len(my_Tuple) == 0:
            my_Tuple = (0, 0)
    elif len(my_Tuple) > 2:
        my_Tuple = (my_Tuple[0], my_Tuple[1])
    return my_Tuple


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_func(tuple_a)
    tuple_b = tuple_func(tuple_b)
    my_Tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return my_Tuple
