#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for i in matrix:
            for j in i[:-1]:
                print("{:d} ".format(j), end="")
            if len(i) != 0:
                print("{:d}".format(i[-1]))
    if matrix[0] == []:
        print("")
