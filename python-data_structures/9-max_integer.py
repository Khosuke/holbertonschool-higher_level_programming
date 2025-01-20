#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return
    biggest_int = my_list[0]
    for i in my_list:
        if biggest_int < i:
            biggest_int = i
    return biggest_int
