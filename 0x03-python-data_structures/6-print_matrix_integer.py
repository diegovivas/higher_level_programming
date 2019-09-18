#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for eachlist in matrix:
            if not eachlist:
                    print()
            for idx, elem in enumerate(eachlist):
                print("{:d}".format(elem), end='')
                if idx != (len(eachlist) - 1):
                    print(" ", end='')
                else:
                    print()
