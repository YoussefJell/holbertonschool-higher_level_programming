#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    try:
        while i < x:
            if type(my_list[i]) is int:
                print(my_list[i], end="")
                j += 1
            i += 1
        print()
    except (ValueError, TypeError):
        print()
        return j
    return j
