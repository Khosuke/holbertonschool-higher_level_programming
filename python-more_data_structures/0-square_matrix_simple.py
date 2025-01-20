#!/usr/bin/python3

def sqr_loop(mtrx_value):
    return mtrx_value**2


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        array_matrix = list(map(sqr_loop, matrix[i]))
        new_matrix.append(array_matrix)
    return new_matrix
