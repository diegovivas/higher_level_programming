#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    for idxs, integer in enumerate(my_list):
        if idxs == idx:
            my_list[idxs] = element
    return my_list
