#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    for elem in my_list:
        newlist.append(elem)
    if idx < 0:
        return newlist
    elif idx > len(my_list) - 1:
        return newlist
    else:
        newlist[idx] = element
        return newlist
