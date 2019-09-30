#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ojo = 0
    for elements in range(x):
        try:
            print(my_list[elements], end="")
            ojo += 1
        except IndexError:
            print()
            return ojo
    print()
    return ojo
