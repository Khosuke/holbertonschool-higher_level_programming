#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print("{:d} ".format(matrix[i][j]), end="")
        try:
            j
        except j.DoesNotExist:
            print("")
        else:
            print("{:d}".format(matrix[i][j]))
