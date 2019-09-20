#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    list2 = list2 + my_list
    for idx, elements in enumerate(list2):
        if elements == search:
            list2[idx] = replace
    return list2
