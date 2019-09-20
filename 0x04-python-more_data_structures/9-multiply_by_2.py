#!/usr/bin/python3
def multiply_by_2(my_dict):
    dict2 = {}
    dict2 = my_dict.copy()
    for keys, value in dict2.items():
        dict2[keys] = value * 2
    return (dict2)
