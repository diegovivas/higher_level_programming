#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for idxs, integer in enumerate(my_list):
        if idxs == idx:
            return integer
    return None
