#!/usr/bin/python3
"""
This is the "matrix_divided" module

This module supplies one function: matrix_divided(). For example,

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix, 2)
[[0.5, 1, 1.5], [2, 2.5, 3]]
"""


def matrix_divided(matrix, div):

    if (not (isinstance(matrix, list)) and 
        not isinstance([row for row in matrix], list) and 
        not isinstance([elem for row in matrix for elem in row], (int, float))):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2), row )) for row in matrix])