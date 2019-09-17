#!/usr/bin/python3
def no_c(my_string):
    a = 0
    for idx, letter in enumerate(my_string):
        if letter == 'c' or letter == 'C':
            new_string = my_string[:idx] + my_string[idx+1:]
            a = 1
    if a == 1:
        return new_string
    return my_string
