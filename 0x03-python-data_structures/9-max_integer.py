#!/usr/bin/python3
def max_integer(my_list=[]):
    Nlist = []
    Nlist = Nlist + my_list
    if my_list:
        Nlist.sort(reverse=True)
        return Nlist[0]
    return None
