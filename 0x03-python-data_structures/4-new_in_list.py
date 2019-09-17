#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    new_list = []
    new_list += my_list
    for idxs, integer in enumerate(new_list):
        if idxs == idx:
            new_list[idxs] = element
            a = 1
    if idx <= idxs:
        return new_list
    else:
        return my_list
