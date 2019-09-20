#!/usr/bin/python3
def best_score(my_dict):

    if my_dict:

        my_list = list(my_dict.values())

        for keys, value in my_dict.items():
            if value == max(my_list):
                return keys
    else:
        return None
