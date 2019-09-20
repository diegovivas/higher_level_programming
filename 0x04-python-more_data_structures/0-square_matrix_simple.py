#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for elements in matrix:
        matrix2 = matrix2 + [[x**2 for x in elements]]
    return (matrix2)
