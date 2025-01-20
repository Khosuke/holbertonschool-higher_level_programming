#!/usr/bin/python3

def no_c(my_string):
    c_less_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            c_less_string += my_string[i]
    return c_less_string
