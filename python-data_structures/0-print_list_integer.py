#!/usr/bin/python3

def print_list_integer(my_list=[]):
    len_list = len(my_list)
    for i in range(0, len_list):
        str = "{}"
        print(str.format(my_list[i]))
