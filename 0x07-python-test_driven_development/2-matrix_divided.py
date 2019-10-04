#!/usr/bin/python3
def matrix_divided(matrix, div):
    final = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    siz = len(matrix[0])
    for x in range(len(matrix)):
        final.append([])
        if type(matrix[x]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if siz != len(matrix[x]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) != int and type(matrix[x][y]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            number = round((matrix[x][y]/3), 2)
            final[x].append(number)
    return final
